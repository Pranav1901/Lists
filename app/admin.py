from typing import List
from django.contrib import admin

from app.models import Category, Item,List

# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(List)

