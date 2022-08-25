from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from .models import Supplier
from .forms import SupplierForm
from .utils import *

from client.models import Address
from client.forms import AddressForm
from utils_global.raw_query_utils import first

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

            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('list-supplier'))


def edit_supplier(request, pk):

    if request.method == 'GET':
        supplier = Supplier.objects.get(pk=pk)
        initial = {
            'corporate_name': supplier.corporate_name,
            'fantasy_name': supplier.fantasy_name,
            'created': supplier.created,
            'cnpj': supplier.cnpj,
            'email': supplier.email,
            'phone_number': supplier.phone_number,
        }
        context = {
            'supplier_form': SupplierForm(initial=initial)
        }
        return render(request, 'supplier/edit_supplier.html', context)

    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST)

        if supplier_form.is_valid():
            updated_supplier = create_supplier_from_supplierform(supplier_form, commit=False)
            updated_supplier.id = pk
            updated_supplier.save(force_update=True)

            messages.success(request, 'Editado Com Sucesso!')

        return HttpResponseRedirect(reverse('list-supplier'))

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
            SELECT SS.*, A.id AS address_id FROM supplier_supplier SS
            LEFT JOIN client_address A ON SS.id = A.supplier_id
        """

        if self.codigo is not None:
            query = query + " WHERE C.id = %s" % str(self.codigo)

        elif self.nome is not None:
            query = query + " WHERE PC.name = %s" % str(self.nome)

        query = query + ' order by id'

        qs = Supplier.objects.raw(query)

        return qs


def detail_supplier(request, pk):

    if request.method == 'GET':

        supplier = Supplier.objects.filter(id=pk).first()

        context = {
            'supplier': supplier
        }

        return render(request, 'supplier/detail_supplier.html', context)


def create_address(request):

    if request.method == 'GET':
        context = {
            'address_form': AddressForm()
        }
        return render(request, 'supplier/address/create_address.html', context)

    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            supplier_id = request.GET.get('fk', None)
            new_address = create_address_from_addressform(address_form, supplier_id=supplier_id, commit=True)

            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('home'))

class ListAddress(ListView):
    model = Address
    template_name = 'supplier/address/list_address.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'address'

    def __init__(self, *args, **kwargs):
        super(ListAddress, self).__init__(*args, **kwargs)
        self.codigo = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ListAddress, self).get_queryset()

        if self.codigo is not None:
            qs = qs.filter(id=self.codigo)

        return qs


def detail_address(request, pk):

    if request.method == 'GET':
        context = dict()

        query = """SELECT A.* FROM client_address A WHERE A.id = %s""" % str(pk)
        context['address'] = first(Address.objects.raw(query))

        return render(request, 'supplier/address/detail_address.html', context)

