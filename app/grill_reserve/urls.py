from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_grill_reserve, name='create-grill-reserve'),
    path('list/', ListGrillReserve.as_view(), name='list-grill-reserve'),
]