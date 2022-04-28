from queue import Empty
from unicodedata import category
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    itemName = models.CharField(max_length=30,blank=False)
    addedBy = models.ForeignKey('auth.User',related_name='item_owner',on_delete=models.CASCADE)
    addedAt = models.DateTimeField(auto_now_add=True,editable=False)
    isCompleted = models.BooleanField(default=False,blank=False)

    def __str__(self):
        return self.itemName


class Category(models.Model):
    categoryName = models.CharField(max_length=30,blank=False)
    addedAt = models.DateTimeField(auto_now_add=True,editable=False)
    noOfList = models.IntegerField(default=0)

    def __str__(self):
        return self.categoryName


class List(models.Model):
    listName = models.CharField(max_length=30,blank=False)
    discription = models.TextField()
    items = models.ManyToManyField(Item)
    collaborators = models.ManyToManyField(User)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    addedAt = models.DateTimeField(auto_now_add=True,editable=False)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.listName
