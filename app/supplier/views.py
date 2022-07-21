from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from supplier.models import Supplier
from supplier.forms import SupplierForm
from supplier.utils import create_supplier_from_supplierform


def create_supplier(request):

    if request.method == 'GET':
        context = {
            'supplier_form': SupplierForm()
        }
        return render(request, 'supplier/create_supplier.html', context)

    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST)

        if supplier_form.is_valid():
            new_supplier = create_supplier_from_supplierform(supplier_form, commit=True)

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


class ListSupplier(ListView):
    model = Supplier
    template_name = 'supplier/list_supplier.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'suppliers'

    def __init__(self, *args, **kwargs):
        super(ListSupplier, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = """
            SELECT SS.* FROM supplier_supplier SS
        """

        if self.codigo is not None:
            query = query + " WHERE C.id = %s" % str(self.codigo)

        elif self.nome is not None:
            query = query + " WHERE PC.name = %s" % str(self.nome)

        qs = Supplier.objects.raw(query)

        return qs


def detail_supplier(request, pk):

    if request.method == 'GET':

        supplier = Supplier.objects.filter(id=pk).first()

        context = {
            'supplier': supplier
        }

        return render(request, 'supplier/detail_supplier.html', context)
