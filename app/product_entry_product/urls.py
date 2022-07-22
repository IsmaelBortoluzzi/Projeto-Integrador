from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_entry_product, name='create-entry-product'),
    path('list/', ListEntryProduct.as_view(), name='list-entry-product'),
    path('delete/', delete_entry_product, name='delete-entry-product'),
]