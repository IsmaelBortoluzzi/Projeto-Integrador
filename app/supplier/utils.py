from .models import Supplier


def create_supplier_from_supplierform(supplier_form, commit=False):
    new_supplier = Supplier()

    new_supplier.corporate_name = supplier_form.cleaned_data.get('corporate_name')
    new_supplier.fantasy_name = supplier_form.cleaned_data.get('fantasy_name')
    new_supplier.created = supplier_form.cleaned_data.get('created')
    new_supplier.cnpj = supplier_form.cleaned_data.get('cnpj')
    new_supplier.email = supplier_form.cleaned_data.get('email')
    new_supplier.phone_number = supplier_form.cleaned_data.get('phone_number')

    if commit is True:
        new_supplier.save()

    return new_supplier

