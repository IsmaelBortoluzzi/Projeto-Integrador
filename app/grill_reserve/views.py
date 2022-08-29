from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from grill_reserve.forms import GrillReserveForm
from grill_reserve.models import GrillReserve


def create_grill_reserve(request):
    if request.method == 'GET':
        context = {
            'grill_reserve_form': GrillReserveForm()
        }
        return render(request, 'grill_reserve/create_grill_reserve.html', context)

    if request.method == 'POST':
        grill_reserve_form = GrillReserveForm(request.POST)

        if grill_reserve_form.is_valid():
            new_grill_reserve = grill_reserve_form.save()

            messages.success(request, 'Salvo Com Sucesso!')

        return HttpResponseRedirect(reverse('list-grill-reserve'))


class ListGrillReserve(ListView):
    model = GrillReserve
    template_name = 'grill_reserve/list_grill_reserve.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'grill_reserves'

    def __init__(self, *args, **kwargs):
        super(ListGrillReserve, self).__init__(*args, **kwargs)
        self.codigo = self.cliente = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.cliente = self.request.GET.get('cliente', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = GrillReserve.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.cliente:
            query = query.filter(id=self.cliente)

        return query
