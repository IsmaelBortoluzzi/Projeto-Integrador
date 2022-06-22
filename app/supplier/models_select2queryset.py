from dal import autocomplete
from django.db import models

from django.conf import settings
from supplier.models import Supplier


class SupplierAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Supplier.objects.none()

        # if not self.request.user.is_authenticated:
        #     return qs
        if self.q:
            self.q = self.q.encode('iso-8859-1', 'ignore').decode('iso-8859-1').upper()

        qs = Supplier.objects.all()

        return qs
