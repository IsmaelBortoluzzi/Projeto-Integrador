from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_product_output, name='create-product-output'),
    path('list/', ListProductOutput.as_view(), name='list-product-output'),
]