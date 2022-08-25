from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.contrib import messages

from product_entry_product.forms import EntryProductModelForm
from product_entry_product.models import EntryProduct


def create_entry_product(request):
    if request.method == 'GET':
        context = {
            'entry_product_form': EntryProductModelForm()
        }
        return render(request, 'entry_product/create_entry_product.html', context)

    if request.method == 'POST':
        entry_product_form = EntryProductModelForm(request.POST)

        if entry_product_form.is_valid():
            new_entry_product = entry_product_form.save()

            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('create-entry-product'))


class ListEntryProduct(ListView):
    model = EntryProduct
    template_name = 'entry_product/list_entry_product.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'entry_products'

    def __init__(self, *args, **kwargs):
        super(ListEntryProduct, self).__init__(*args, **kwargs)
        self.codigo = self.document = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.document = self.request.GET.get('document', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = EntryProduct.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.document:
            query = query.filter(entry_document__id=self.document)

        return query


def delete_entry_product(request, pk):
    entry_product = EntryProduct.objects.filter(pk=pk).first()

    if entry_product:
        entry_product.delete()

        messages.success(request, 'Deletado Com Sucesso!')

    return HttpResponseRedirect(reverse('list-entry-product'))

