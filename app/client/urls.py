from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_client, name='create-client'),
    path('list/', ListClient.as_view(), name='list-client'),
    path('edit/<int:pk>/', edit_client, name='edit-client'),
    path('delete/<int:pk>/', delete_client, name='delete-client'),

    # Address
    path('address/create/', create_address, name='create-address'),
    path('address/list/', ListAddress.as_view(), name='list-address'),
    path('address/detail/<int:pk>/', detail_address, name='detail-address'),
]