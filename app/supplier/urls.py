from django.urls import path, include

from .models_select2queryset import SupplierAutocomplete
from .views import *

urlpatterns = [

    # autocomplete
    path('supplier-autocomplete/', SupplierAutocomplete.as_view(), name='supplier-autocomplete')
]
