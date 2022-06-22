from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .forms import ClientForm, AddressForm
from .models import Client, Address
from .utils import (
    create_client_from_clientform,
    create_address_from_addressform,
)
from utils_global.raw_query_utils import first


#  CLIENT VIEWS

def create_client(request):

    if request.method == 'GET':
        context = {
            'client_form': ClientForm()
        }
        return render(request, 'client/create_client.html', context)

    if request.method == 'POST':
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            new_client = create_client_from_clientform(client_form, commit=True)

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


def edit_client(request):
    # TODO Fazer o edit client
    pass


class ListClient(ListView):
    model = Client
    template_name = 'client/list_client.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'clients'

    def __init__(self, *args, **kwargs):
        super(ListClient, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = """
            SELECT C.*, A.id AS address_id FROM client_client C
            LEFT JOIN client_address A ON C.id = A.id
        """

        if self.codigo is not None:
            query = query + " WHERE C.id = %s" % str(self.codigo)

        qs = Client.objects.raw(query)

        return qs


# ADDRESS VIEWS


def create_address(request):

    if request.method == 'GET':
        context = {
            'address_form': AddressForm()
        }
        return render(request, 'client/address/create_address.html', context)

    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            client_id = request.GET.get('fk', None)
            new_address = create_address_from_addressform(address_form, client_id=client_id, commit=True)

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


# PermissionRequiredMixin,
class ListAddress(ListView):
    model = Address
    template_name = 'client/address/list_address.html'
    # permission_required = ''
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


def detail_address(request, pk):  # pk: address primary key

    if request.method == 'GET':
        context = dict()

        query = """SELECT A.* FROM client_address A WHERE A.id = %s""" % str(pk)
        address = Address.objects.raw(query)

        context['address'] = first(address)  # pega o primero address

        return render(request, 'client/address/detail_address.html', context)

