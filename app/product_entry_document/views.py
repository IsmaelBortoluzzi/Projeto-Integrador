from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .forms import EntryDocumentForm, InlineDocumentProductForm
from .models import EntryDocument


def create_entry_document(request):
    if request.method == 'GET':
        context = {
            'entry_document_form': InlineDocumentProductForm(),
        }
        return render(request, 'entry_document/create_entry_document.html', context)

    if request.method == 'POST':
        entry_document_form = InlineDocumentProductForm(request.POST)

        if entry_document_form.is_valid():
            new_entry_document = entry_document_form.save()

        # TODO importar o messages pra dizer pro user pq o form veio inválido

        return HttpResponseRedirect(reverse('home'))


class ListEntryDocument(ListView):
    model = EntryDocument
    template_name = 'entry_document/list_entry_document.html'
    paginate_by = 15
    extra_context = dict()
    context_object_name = 'entry_documents'

    def __init__(self, *args, **kwargs):
        super(ListEntryDocument, self).__init__(*args, **kwargs)
        self.codigo = self.document_type = None

    def get(self, request, *args, **kwargs):
        self.codigo = self.request.GET.get('codigo', None)
        self.document_type = self.request.GET.get('document_type', None)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = EntryDocument.objects.all()

        if self.codigo:
            query = query.filter(id=self.codigo)
        if self.document_type:
            query = query.filter(id=self.document_type)

        return query




