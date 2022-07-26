from product_entry_document.models import EntryDocument
from product_entry_product.models import EntryProduct


def create_entry_document_with_one_product(entry_document_product, commit=True):
    new_entry_document = EntryDocument()
    new_entry_product = EntryProduct()

    new_entry_document.document_number = entry_document_product.cleaned_data.get('document_number')
    new_entry_document.document_type = entry_document_product.cleaned_data.get('document_type')
    new_entry_document.total_value = entry_document_product.cleaned_data.get('total_value')
    new_entry_document.emission_date = entry_document_product.cleaned_data.get('emission_date')
    new_entry_document.supplier = entry_document_product.cleaned_data.get('supplier')

    new_entry_product.quantity = entry_document_product.cleaned_data.get('quantity')
    new_entry_product.cost = entry_document_product.cleaned_data.get('cost')
    new_entry_product.product = entry_document_product.cleaned_data.get('product')

    if commit is True:
        new_entry_document.save()

        new_entry_product.entry_document = new_entry_document
        new_entry_product.save()

    return new_entry_document, new_entry_product
