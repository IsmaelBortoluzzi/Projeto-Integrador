from django.urls import path
from product_brand.views import *

urlpatterns = [
    path('create-brand/', create_brand, name='create-brand'),
    path('list-brand/', ListBrand.as_view(), name='list-brand'),
]