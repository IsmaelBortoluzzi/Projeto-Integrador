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
