from .models import Client, Address

# CLIENT UTILS


def create_client_from_clientform(client_form, commit=False):
    new_client = Client()

    new_client.full_name = client_form.cleaned_data.get('full_name')
    new_client.nickname = client_form.cleaned_data.get('nickname')
    new_client.birth_date = client_form.cleaned_data.get('birth_date')
    new_client.cpf = client_form.cleaned_data.get('cpf')
    new_client.phone_number = client_form.cleaned_data.get('phone_number')
    new_client.address = None

    if commit is True:
        new_client.save()

    return new_client


# ADDRESS UTILS

def create_address_from_addressform(address_form, client_id, commit=False):
    new_address = Address()

    new_address.cep = address_form.cleaned_data.get('cep')
    new_address.street = address_form.cleaned_data.get('street')
    new_address.number = address_form.cleaned_data.get('number')
    new_address.district = address_form.cleaned_data.get('district')
    new_address.city = address_form.cleaned_data.get('city')
    new_address.state = address_form.cleaned_data.get('state')
    new_address.client = Client.objects.filter(id=client_id).first()

    if commit is True:
        new_address.save()

    return new_address

