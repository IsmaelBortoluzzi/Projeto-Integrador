from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_bills_tobe_paid, name='create-bills-tobe-paid'),
    path('list/', ListBillsToBePaid.as_view(), name='list-bills-tobe-paid'),
    path('pay/<int:pk>', pay_bills_tobe_paid, name='pay-bills_tobe_paid'),
]