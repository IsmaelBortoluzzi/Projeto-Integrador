from django.contrib import messages
from django.db.models import Subquery, OuterRef, Sum
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from order.forms import InlineOrderProductForm, OrderForm
from order.models import Order
from order.utils import create_order_with_one_product
from product.models import Product
from product_output.models import ProductOutput


def create_order(request):
    if request.method == 'GET':
        context = {
            'order_form': InlineOrderProductForm(),
        }
        return render(request, 'order/create_order.html', context)

    if request.method == 'POST':
        order_form = InlineOrderProductForm(request.POST)

        if order_form.is_valid():
            new_order = create_order_with_one_product(order_form, commit=True)

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar sua comanda!')

        return HttpResponseRedirect(reverse('home'))


class ListOrder(ListView):
    model = Order
    template_name = 'order/list_order.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'orders'

    def __init__(self, *args, **kwargs):
        super(ListOrder, self).__init__(*args, **kwargs)
        self.codigo =  None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = """
            select oo.*, sum(T.total) as total from order_order oo
            join (
                select pop.order_id, (pop.quantity * pp.selling_price) as total 
                from product_output_productoutput pop
                join product_product pp
                on pop.product_id = pp.id
            ) T
            on T.order_id = oo.id
        """

        if self.codigo is not None:
            query = query + " where oo.id = %s" % str(self.codigo)

        query = Order.objects.raw(query + " group by oo.id;")

        return query


def edit_order(request):
    if request.method == 'GET':
        pk = int(request.GET.get('order'))
        context = {
            'order_form': OrderForm(instance=Order.objects.get(pk=pk))
        }
        return render(request, 'order/edit_order.html', context)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            updated_order = order_form.save(commit=False)
            updated_order.id = int(request.GET.get('order'))
            updated_order.save(force_update=True)

        messages.success(request, 'Editado Com Sucesso!')

        return HttpResponseRedirect(reverse('list-order'))

