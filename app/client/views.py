from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .forms import ClientForm
from .models import Client
from .utils import create_client_from_clientform


def create_client(request):

    if request.method == 'GET':
        context = {
            'client_form': ClientForm()
        }
        return render(request, 'client/create_client.html', context)

    if request.method == 'POST':
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            new_client = create_client_from_clientform(client_form, commit=True)

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


class ListClient(ListView):
    model = Client
    template_name = 'client/list_client.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'clients'

    def __init__(self, *args, **kwargs):
        super(ListClient, self).__init__(*args, **kwargs)
        self.codigo = self.nome = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.nome = self.request.GET.get('nome', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ListClient, self).get_queryset()

        if self.codigo is not None:
            qs = qs.filter(id=self.codigo)

        elif self.nome is not None:
            qs = qs.filter(first_name=self.nome)

        return qs

