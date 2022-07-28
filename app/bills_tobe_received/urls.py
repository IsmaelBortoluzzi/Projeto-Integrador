from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_bills_received, name='create-bills-tobe-received'),
    path('list/', ListBillsToBeReceived.as_view(), name='list-bills-tobe-received'),
    path('receive/<int:pk>', receive_bills_tobe_received, name='receive-bills-tobe-received'),
]