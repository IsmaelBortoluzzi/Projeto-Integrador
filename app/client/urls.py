from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_client, name='create-client'),
    path('list/', ListClient.as_view(), name='list-client'),
]