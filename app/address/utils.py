from address.models import Address


def create_address_from_addressform(address_form, commit=False):
    new_address = Address()

    new_address.cep = address_form.data.get('cep')
    new_address.street = address_form.data.get('street')
    new_address.number = address_form.data.get('number')
    new_address.district = address_form.data.get('district')
    new_address.city = address_form.data.get('city')
    new_address.state = address_form.data.get('state')

    if commit is True:
        new_address.save()

    return new_address
