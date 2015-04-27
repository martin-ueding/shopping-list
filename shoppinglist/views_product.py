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

def add(request, shelf_id):
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
