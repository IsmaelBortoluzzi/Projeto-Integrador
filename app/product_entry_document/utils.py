from product_entry_document.models import EntryDocument


def create_entry_document_with_one_product(entry_document, entry_product):
    new_entry_document = EntryDocument()

    new_entry_document.document_number = entry_document.cleaned_data.get('document_number')
    new_entry_document.document_type = entry_document.cleaned_data.get('document_type')
    new_entry_document.total_value = entry_document.cleaned_data.get('total_value')
    new_entry_document.emission_date = entry_document.cleaned_data.get('emission_date')
    new_entry_document.db_registration_date = entry_document.cleaned_data.get('db_registration_date')
    # new_entry_document.supplier = entry_document.cleaned_data.get('')