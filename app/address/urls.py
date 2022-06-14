from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_address, name='create-address'),
    path('list/', ListAddress.as_view(), name='list-address'),
    path('detail/<int:pk>/', detail_address, name='detail-address'),
]