from django.contrib import admin
from .models import ShoppingItem, ShoppingList


admin.site.register(ShoppingItem)
admin.site.register(ShoppingList)
