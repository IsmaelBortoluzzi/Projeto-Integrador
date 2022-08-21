from django.urls import path

from .views import *

urlpatterns = [
    path('create-supplier', create_supplier, name='create-supplier'),
    path('list-supplier/', ListSupplier.as_view(), name='list-supplier'),
    path('edit/<int:pk>', edit_supplier, name='edit-supplier'),
    path('detail-supplier/<int:pk>/', detail_supplier, name='detail-supplier'),

    path('address/create/', create_address, name='create-supplier-address'),
    path('address/list/', ListAddress.as_view(), name='list-supplier-address'),
    path('address/detail/<int:pk>/', detail_address, name='detail-supplier-address'),
]
