from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_product, name='create-product'),
    path('list/', ListProduct.as_view(), name='list-product'),
    path('edit/<int:pk>', edit_product, name='edit-product'),
]