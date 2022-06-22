from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from product_brand.forms import BrandForm, BrandEditForm
from product_brand.models import Brand
from product_brand.utils import create_brand_from_brandform, create_brand_from_brandeditform


def create_brand(request):

    if request.method == 'GET':
        context = {
            'brand_form': BrandForm()
        }
        return render(request, 'brand/create_brand.html', context)

    if request.method == 'POST':
        brand_from = BrandForm(request.POST)

        if brand_from.is_valid():
            new_brand = create_brand_from_brandform(brand_from, commit=True)

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


class ListBrand(ListView):
    model = Brand
    template_name = 'brand/list_brand.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'brands'

    def __init__(self, *args, **kwargs):
        super(ListBrand, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = """
            SELECT PC.*, SS.id AS supplier_id FROM product_brand PC
            LEFT JOIN supplier_supplier SS ON PC.id = SS.id
        """

        if self.codigo is not None:
            query = query + " WHERE C.id = %s" % str(self.codigo)

        elif self.nome is not None:
            query = query + " WHERE PC.name = %s" % str(self.nome)

        query = query + " ORDER BY PC.is_active DESC"

        qs = Brand.objects.raw(query)

        return qs


def edit_brand(request, pk):

    if request.method == 'GET':

        brand = Brand.objects.filter(id=pk).select_related('supplier').first()

        if brand is None:
            raise ValueError('marca não existe!')

        initial = {
            'name': brand.name,
            'initials': brand.initials,
            'supplier': brand.supplier,
            'is_active': brand.is_active,
        }

        context = {
            'brand_form': BrandEditForm(initial=initial)
        }

        return render(request, 'brand/create_brand.html', context)

    if request.method == 'POST':
        brand_edit_from = BrandEditForm(request.POST)

        if brand_edit_from.is_valid():
            new_brand = create_brand_from_brandeditform(brand_edit_from, pk, commit=True)

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('list-brand'))
