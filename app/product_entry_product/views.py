from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

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

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


class ListEntryProduct(ListView):
    model = EntryProduct
    template_name = 'entry_product/list_entry_product.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'entry_products'

    def __init__(self, *args, **kwargs):
        super(ListEntryProduct, self).__init__(*args, **kwargs)
        self.codigo = self.document_id = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.document_id = self.request.GET.get('document_id', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = EntryProduct.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.document_id:
            query = query.filter(document_id__id=self.document_id)

        return query


def delete_entry_product(request, pk):
    entry_product = EntryProduct.objects.filter(pk=pk).first()

    if entry_product:
        entry_product.delete()

    return HttpResponseRedirect(reverse('list-entry_product'))

