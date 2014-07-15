from django.shortcuts import render, render_to_response, redirect

from shoppinglist.models import Product, Shelf

# Create your views here.

def index(request):
    shelves = Shelf.objects.all()
    shelves_template = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all()]
        if len(products) > 0:
            products.sort()
            shelves_template.append((shelf.name, products))

    return render_to_response('shoppinglist/index.html', {'shelves': shelves_template})

def view(request):
    #needed = Product.objects.filter(desired_amount__gt=0)
    shelves = Shelf.objects.all()

    shelves_needed = []

    for shelf in sorted(shelves):
        products = [product for product in shelf.product_set.all() if product.is_needed()]
        if len(products) > 0:
            products.sort()
            shelves_needed.append((shelf.name, products))

    return render_to_response('shoppinglist/view.html', {'shelves_needed': shelves_needed})

def change(request, product_id, delta):
    product = Product.objects.filter(id=product_id)[0]
    delta = int(delta)
    if product.desired_amount + delta >= 0:
        product.desired_amount += delta
        product.save()
    return redirect('/shopping/#product{}'.format(product_id))
