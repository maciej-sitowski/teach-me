import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from shopping_list.models import ShoppingList


@pytest.mark.django_db
def test_shopping_list_creation():
    url = reverse('all-shopping-lists')
    data = {
        'name': 'Groceries',
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert ShoppingList.objects.get().name == 'Groceries'


@pytest.mark.django_db
def test_shopping_list_creation_missing_field():
    url = reverse('all-shopping-lists')
    data = {
        'different_field': 'Groceries',
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_shopping_list_creation_additional_field():
    url = reverse('all-shopping-lists')
    data = {
        'name': 'Groceries',
        'different_field': 'diff',
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert ShoppingList.objects.get().name == 'Groceries'
    assert not hasattr(ShoppingList.objects.get(), "different_field")
