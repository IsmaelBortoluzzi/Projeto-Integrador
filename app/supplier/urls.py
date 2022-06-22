from django.urls import path, include

from .models_select2queryset import SupplierAutocomplete
from .views import *

urlpatterns = [
    path('list-supplier/', ListSupplier.as_view(), name='list-supplier'),
    path('detail-supplier/<int:pk>/', detail_supplier, name='detail-supplier'),
    # autocomplete
    path('supplier-autocomplete/', SupplierAutocomplete.as_view(), name='supplier-autocomplete')
]
