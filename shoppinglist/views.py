#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>

import re

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from shoppinglist.models import Product, Shelf

ID_PATTERN = re.compile(r'id-(\d+)')

@login_required
def index(request):
    shelves = Shelf.objects.all()
    shelves_template = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all()]
        products.sort()
        shelves_template.append((shelf.name, shelf.id, products))

    return render_to_response('shoppinglist/templates/list/edit.html',
                              {'shelves': shelves_template},
                              context_instance=RequestContext(request))

@login_required
def view(request):
    shelves = Shelf.objects.all()

    shelves_needed = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all() if product.is_needed()]
        if len(products) > 0:
            products.sort()
            shelves_needed.append((shelf.name, products))

    return render_to_response('shoppinglist/templates/list/view.html',
                              {'shelves_needed': shelves_needed})

class ShelfForm(ModelForm):
    class Meta:
        model = Shelf


@login_required
def add_shelf(request):
    if request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shoppinglist.views.index'))
    else:
        form = ShelfForm()
        for field in form.fields:
            form[field].css_classes('form-control')
            print(field, form[field].css_classes())

    return render_to_response(
        'shoppinglist/templates/shelf/new.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

@login_required
def aftermath(request):
    resetted = []
    if 'product_ids' in request.POST:
        for product_id in request.POST.getlist('product_ids'):
            id = int(product_id)

            product = Product.objects.filter(id=id)[0]
            product.desired_amount = 0
            product.save()
            resetted.append(product.name)

    products = [product for product in Product.objects.all() if product.is_needed()]
    if len(products) > 0:
        products.sort()

    return render_to_response('shoppinglist/templates/list/aftermath.html',
                              {'products': products, 'resetted': resetted},
                              context_instance=RequestContext(request))

@login_required
def update_numbers(request):
    for key in request.POST:
        match = ID_PATTERN.match(key)
        if not match:
            continue

        product_id = int(match.group(1))
        product = Product.objects.filter(id=product_id)[0]
        delta = int(request.POST[key])

        if delta == 0:
            continue

        product.desired_amount += delta
        product.save()
    return HttpResponseRedirect(reverse('shoppinglist.views.index'))
