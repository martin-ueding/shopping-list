from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from shoppinglist.models import Product, Shelf

import re

ID_PATTERN = re.compile(r'id-(\d+)')

def index(request):
    shelves = Shelf.objects.all()
    shelves_template = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all()]
        products.sort()
        shelves_template.append((shelf.name, shelf.id, products))

    return render_to_response('shoppinglist/index.html',
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

    return render_to_response('shoppinglist/view.html',
                              {'shelves_needed': shelves_needed})

def add_product(request, shelf_id):
    name = request.POST['name']
    if len(name) > 0:
        shelf = Shelf.objects.filter(id=shelf_id)[0]
        product = Product(name=name, shelf=shelf)
        product.save()
    return HttpResponseRedirect(reverse('shoppinglist.views.index'))

def add_shelf(request):
    name = request.POST['name']
    if len(name) > 0:
        shelf = Shelf(name=name, rank=-1)
        shelf.save()
    return HttpResponseRedirect(reverse('shoppinglist.views.index'))

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

    return render_to_response('shoppinglist/aftermath.html',
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
