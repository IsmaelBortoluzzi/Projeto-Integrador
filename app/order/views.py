from django.contrib import messages
from django.db.models import Subquery, OuterRef, Sum
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from order.forms import InlineOrderProductForm
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

        return HttpResponseRedirect(reverse('home'))


class ListOrder(ListView):
    model = Order
    template_name = 'order/list_order.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'orders'

    def __init__(self, *args, **kwargs):
        super(ListOrder, self).__init__(*args, **kwargs)
        self.codigo = self.document_type = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.document_type = self.request.GET.get('document_type', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = Order.objects.all()
        """
        select sum(T.total) from order_order oo
        join (
            select pop.order_id, pop.quantity, pp.selling_price,
                   (pop.quantity * pp.selling_price) as total from product_output_productoutput pop
        
            join product_product pp
            on pop.product_id = pp.id
        ) T
        on T.order_id = oo.id
        where oo.id = 4;
        """

        oi = list(query)

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.document_type:
            query = query.filter(id=self.document_type)

        return query





