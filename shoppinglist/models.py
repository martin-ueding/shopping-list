#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © YEAR Martin Ueding <dev@martin-ueding.de>


'''
Models.
'''

import json

from django.db import models

# Create your models here.

class Shelf(models.Model):
    '''
    A shelf in a store.
    '''
    name = models.CharField(max_length=200, unique=True)
    rank = models.IntegerField()

    def __unicode__(self):
        return u'{} (Rank {})'.format(self.name, self.rank)

    def __lt__(self, other):
        return self.rank < other.rank

class Product(models.Model):
    '''
    A single product from a store.
    '''
    name = models.CharField(max_length=200)
    desired_amount = models.IntegerField(default=0)
    shelf = models.ForeignKey(Shelf)

    def __unicode__(self):
        return u'{} @ {} (×{})'.format(self.name, self.shelf.name, self.desired_amount)

    def __lt__(self, other):
        return self.name < other.name

    def is_needed(self):
        return self.desired_amount > 0

def import_json(filename):
    with open(filename) as f:
        data = json.load(f)

    for shelf, products in data.iteritems():
        shelf_db_list = Shelf.objects.filter(name__icontains=shelf)
        if len(shelf_db_list) == 1:
            shelf_db = shelf_db_list[0]
        else:
            shelf_db = Shelf(name=shelf, rank=0)
            shelf_db.save()

        for product in products:
            p = Product(name=product, shelf=shelf_db)
            p.save()


