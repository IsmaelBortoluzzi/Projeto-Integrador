from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from order.forms import OrderForm, OrderPaymentForm
from order.models import Order


def create_order(request):
    if request.method == 'GET':
        context = {
            'order_form': OrderForm(),
        }
        return render(request, 'order/create_order.html', context)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            new_order = order_form.save()

            messages.success(request, 'Salvo Com Sucesso!')
        else:
            messages.error(request, 'Não foi possível salvar sua comanda!')

        return HttpResponseRedirect(reverse('list-order'))


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
            select oo.*, COALESCE((select sum(quantity * sold_price) from product_output_productoutput where order_id = oo.id group by order_id), 0.00)
            as total from order_order oo where oo.is_active = True order by oo.id
        """
        query = Order.objects.raw(query)

        return query


def edit_order(request, pk):
    if request.method == 'GET':
        context = {
            'order_form': OrderPaymentForm(instance=Order.objects.get(pk=pk))
        }
        return render(request, 'order/edit_order.html', context)

    if request.method == 'POST':

        updated_order = Order.objects.filter(pk=pk)
        updated_order.update(payment_form = request.POST['payment_form'])
        updated_order.update(is_active = False)

        messages.success(request, 'Pagamento efetuado!')

        return HttpResponseRedirect(reverse('list-order'))

