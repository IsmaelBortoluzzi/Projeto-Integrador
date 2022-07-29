from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_order, name='create-order'),
    path('list/', ListOrder.as_view(), name='list-order'),
]