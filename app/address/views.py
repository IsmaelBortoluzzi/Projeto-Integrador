from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from .forms import AddressForm
from .models import Address
from .utils import create_address_from_addressform


def create_address(request):

    if request.method == 'GET':
        context = {
            'address_form': AddressForm()
        }
        return render(request, 'address/create_address.html', context)

    if request.method == 'POST':
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            new_address = create_address_from_addressform(address_form, commit=True)

        return HttpResponseRedirect(reverse('home'))


# def list_address(request):
#     if request.method == 'GET':
#         paginator = DiggPaginator(context['clientes'], 15, body=5)
#         page = request.GET.get('page', 1)
#         context['is_paged'] = paginator.num_pages > 1
#
#         try:
#             context['clientes'] = paginator.page(page)
#         except (InvalidPage, TypeError):
#             context['clientes'] = paginator.page(1)


# PermissionRequiredMixin,
class ListAddress(ListView):
    model = Address
    template_name = 'address/list_address.html'
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

        query = """SELECT A.* FROM address_address A WHERE id = %s""" % str(pk)
        address = Address.objects.raw(query)

        context['address'] = address

        return render(request, 'address/detail_address.html', context)


