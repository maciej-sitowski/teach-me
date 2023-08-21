from django.urls import path
from shopping_list.api.views import ListAddShoppingList, ShoppingListDetail, AddShoppingItem, RetrieveShoppingItem


urlpatterns = [
    path("shopping-lists/", ListAddShoppingList.as_view(), name='all-shopping-lists'),
    path("shopping-lists/<uuid:pk>/", ShoppingListDetail.as_view(), name='shopping_list_detail'),
    path("shopping-lists/<uuid:pk>/shopping-items/", AddShoppingItem.as_view(), name='shopping_list_detail'),
    path("shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", RetrieveShoppingItem.as_view(), name='shopping_list_detail'),
]

