from django.contrib import admin

# Register your models here.
# I wrote code below

from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)