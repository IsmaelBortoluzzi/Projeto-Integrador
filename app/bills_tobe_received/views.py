from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DeleteView

from .forms import BillsToBeReceivedForm
from .models import BillsToBeReceived


def create_bills_received(request):
    if request.method == 'GET':
        context = {
            'bills_tobe_received_form': BillsToBeReceivedForm()
        }
        return render(request, 'bills_tobe_received/create_bills_tobe_received.html', context)

    if request.method == 'POST':
        bills_tobe_received_form = BillsToBeReceivedForm(request.POST)

        if bills_tobe_received_form.is_valid():
            new_bills_tobe_received = bills_tobe_received_form.save()

            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('home'))


class ListBillsToBeReceived(ListView):
    model = BillsToBeReceived
    template_name = 'bills_tobe_received/list_bills_tobe_received.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'bills_tobe_received'

    def __init__(self, *args, **kwargs):
        super(ListBillsToBeReceived, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = BillsToBeReceived.objects.all().select_related('order_id')

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.nome:
            query = query.filter(id=self.nome)

        return query


def receive_bills_tobe_received(request, pk):

    if request.method == 'GET':
        bill = BillsToBeReceived.objects.get(pk=pk)
        bill.remaining_value = 0.0
        bill.save()

        messages.success(request, 'Recebido Com Sucesso!')

    return HttpResponseRedirect(reverse('list-bills-tobe-received'))
