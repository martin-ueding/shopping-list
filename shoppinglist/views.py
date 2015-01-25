#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014-2015 Martin Ueding <dev@martin-ueding.de>

import re

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.forms import ModelForm

from shoppinglist.models import Product, Shelf

ID_PATTERN = re.compile(r'id-(\d+)')

def index(request):
    shelves = Shelf.objects.all()
    shelves_template = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all()]
        products.sort()
        shelves_template.append((shelf.name, shelf.id, products))

    return render_to_response('shoppinglist/templates/index.html',
                              {'shelves': shelves_template},
                              context_instance=RequestContext(request))

def view(request):
    shelves = Shelf.objects.all()

    shelves_needed = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all() if product.is_needed()]
        if len(products) > 0:
            products.sort()
            shelves_needed.append((shelf.name, products))

    return render_to_response('shoppinglist/templates/view.html',
                              {'shelves_needed': shelves_needed})

class ProductForm(ModelForm):
    class Meta:
        model = Product

class ShelfForm(ModelForm):
    class Meta:
        model = Shelf

def add_product(request, shelf_id):
    shelf = Shelf.objects.filter(id=shelf_id)[0]

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shoppinglist.views.index'))
    else:
        form = ProductForm(initial={'shelf': shelf})

    return render_to_response(
        'shoppinglist/templates/new-product.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

def add_shelf(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) > 0:
            shelf = Shelf(name=name, rank=-1)
            shelf.save()
        return HttpResponseRedirect(reverse('shoppinglist.views.index'))
    else:
        form = ShelfForm()
        for field in form.fields:
            form[field].css_classes('form-control')
            print(field, form[field].css_classes())
        return render_to_response(
            'shoppinglist/templates/new-shelf.html',
            {'form': form},
            context_instance=RequestContext(request),
        )

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

    return render_to_response('shoppinglist/templates/aftermath.html',
                              {'products': products, 'resetted': resetted},
                              context_instance=RequestContext(request))

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
