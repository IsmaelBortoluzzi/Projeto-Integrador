from address.models import Address


def create_address_from_addressform(address_form, commit=False):
    new_address = Address()

    new_address.cep = address_form.cleaned_data.get('cep')
    new_address.street = address_form.cleaned_data.get('street')
    new_address.number = address_form.cleaned_data.get('number')
    new_address.district = address_form.cleaned_data.get('district')
    new_address.city = address_form.cleaned_data.get('city')
    new_address.state = address_form.cleaned_data.get('state')

    if commit is True:
        new_address.save()

    return new_address
