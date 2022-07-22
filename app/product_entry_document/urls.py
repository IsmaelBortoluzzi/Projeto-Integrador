from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', create_entry_document, name='create-entry-document'),
    path('list/', ListEntryDocument.as_view(), name='list-entry-document'),
]