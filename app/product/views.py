from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .forms import ProductForm, ProductEditForm
from .models import Product

#  CLIENT VIEWS

def create_product(request):

    if request.method == 'GET':
        context = {
            'product_form': ProductForm()
        }
        return render(request, 'product/create_product.html', context)

    if request.method == 'POST':
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            new_product = product_form.save()
            messages.success(request, 'Salvo Com Sucesso!')

            return HttpResponseRedirect(reverse('list-product'))

        else:
            return render(request, 'product/edit_product.html', product_form)


def edit_product(request, pk):

    if request.method == 'GET':
        context = {
            'product_form': ProductEditForm(instance=Product.objects.get(pk=pk))
        }
        return render(request, 'product/edit_product.html', context)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST)

        if product_form.is_valid():
            updated_product = product_form.save(commit=False)
            updated_product.id = pk
            updated_product.save(force_update=True)
            messages.success(request, 'Editado Com Sucesso!')

            return HttpResponseRedirect(reverse('list-product'))

        else:
            messages.error(request, 'Erros nos dados!')
            return render(request, 'product/edit_product.html', product_form)


class ListProduct(ListView):
    model = Product
    template_name = 'product/list_product.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'products'

    def __init__(self, *args, **kwargs):
        super(ListProduct, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = Product.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.nome:
            query = query.filter(id=self.nome)

        return query

