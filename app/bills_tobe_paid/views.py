from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DeleteView

from .forms import BillsToBePaidForm
from .models import BillsToBePaid


def create_bills_tobe_paid(request):
    if request.method == 'GET':
        context = {
            'bills_tobe_paid_form': BillsToBePaidForm()
        }
        return render(request, 'bills_tobe_paid/create_bills_tobe_paid.html', context)

    if request.method == 'POST':
        bills_tobe_paid_form = BillsToBePaidForm(request.POST)

        if bills_tobe_paid_form.is_valid():
            new_bills_tobe_paid = bills_tobe_paid_form.save()

            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('home'))


class ListBillsToBePaid(ListView):
    model = BillsToBePaid
    template_name = 'bills_tobe_paid/list_bills_tobe_paid.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'bills_tobe_paid'

    def __init__(self, *args, **kwargs):
        super(ListBillsToBePaid, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = BillsToBePaid.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.nome:
            query = query.filter(id=self.nome)
        
        return query


def pay_bills_tobe_paid(request, pk):

    if request.method == 'GET':
        bill = BillsToBePaid.objects.get(pk=pk)
        bill.is_paid = True
        bill.save()

        messages.success(request, 'Paga Com Sucesso!')

    return HttpResponseRedirect(reverse('list-bills-tobe-paid'))
