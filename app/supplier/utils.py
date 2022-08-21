from .models import Supplier
from client.models import Address


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

def create_address_from_addressform(address_form, supplier_id, commit=False):
    new_address = Address()

    new_address.cep = address_form.cleaned_data.get('cep')
    new_address.street = address_form.cleaned_data.get('street')
    new_address.number = address_form.cleaned_data.get('number')
    new_address.district = address_form.cleaned_data.get('district')
    new_address.city = address_form.cleaned_data.get('city')
    new_address.state = address_form.cleaned_data.get('state')
    new_address.supplier = Supplier.objects.filter(id=supplier_id).first()

    if commit is True:
        new_address.save()

    return new_address

