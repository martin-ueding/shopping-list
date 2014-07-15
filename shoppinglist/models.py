'''
Models.
'''

from django.db import models

# Create your models here.

class Shelf(models.Model):
    '''
    A shelf in a store.
    '''
    name = models.CharField(max_length=200, unique=True)
    rank = models.IntegerField(default=0)

    def __unicode__(self):
        return u'{} (Rank {})'.format(self.name, self.rank)

class Product(models.Model):
    '''
    A single product from a store.
    '''
    name = models.CharField(max_length=200)
    desired_amount = models.IntegerField()
    shelf = models.ForeignKey(Shelf)

    def __unicode__(self):
        return u'{} @ {}'.format(self.name, self.shelf.name)
