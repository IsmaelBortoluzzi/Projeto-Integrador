from dal import autocomplete
from django.db import models

from django.conf import settings
from supplier.models import Supplier


class SupplierAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Supplier.objects.none()

        if not self.request.user.is_authenticated:
            return qs

        qs = Supplier.objects.all()

        return qs
