from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.contrib import messages

from product_output.forms import ProductOutputModelForm
from product_output.models import ProductOutput

def create_product_output(request):
    if request.method == 'GET':
        context = {
            'product_output_form': ProductOutputModelForm()
        }
        return render(request, 'product_output/create_product_output.html', context)

    if request.method == 'POST':
        product_output_form = ProductOutputModelForm(request.POST)

        if product_output_form.is_valid():
            new_product_output = product_output_form.save(commit=False)

            if new_product_output.quantity > new_product_output.product_id.current_inventory - new_product_output.product_id.minimum_inventory:
                messages.error(request, 'Não tem estoque suficiente!')
                return HttpResponseRedirect(reverse('create-product-output'))

            if new_product_output.product_id.current_inventory - new_product_output.quantity < (new_product_output.product_id.current_inventory - new_product_output.product_id.minimum_inventory) * 0.1:
                messages.warning(request, 'Cuidado! O estoque deste produto está baixo!')

            new_product_output.save()
            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('create-product-output'))


class ListProductOutput(ListView):
    model = ProductOutput
    template_name = 'product_output/list_product_output.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'product_outputs'

    def __init__(self, *args, **kwargs):
        super(ListProductOutput, self).__init__(*args, **kwargs)
        self.codigo = self.order = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.order = self.request.GET.get('order', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = ProductOutput.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.order:
            query = query.filter(order__id=self.order)
        return query

