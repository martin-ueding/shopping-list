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


class ProductForm(ModelForm):
    class Meta:
        model = Product

def add(request, shelf_id=None):
    shelf = None
    if shelf_id is not None:
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


def order_more(request, product_id_str):
    product_id = int(product_id_str)
    product = Product.objects.filter(id=product_id)[0]
    return render_to_response(
        'shoppinglist/templates/order-more.html',
        {'product_id': product_id,
         'name': product.name,
         'desired': product.desired_amount,
         'range1': range(2, 5),
         'range2': range(5, 11)
        },
        context_instance=RequestContext(request),
    )


def increment(request, product_id_str, delta):
    product_id = int(product_id_str)
    product = Product.objects.filter(id=product_id)[0]
    product.desired_amount += int(delta)
    product.save()

    return HttpResponseRedirect(reverse('shoppinglist.views.index'))


def index(request):
    products = Product.objects.all()

    return render_to_response('shoppinglist/templates/product/index.html',
                              {'products': products},
                              context_instance=RequestContext(request))
