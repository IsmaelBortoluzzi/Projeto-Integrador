from .models import Client


def create_client_from_clientform(client_form, commit=False):
    new_client = Client()

    new_client.first_name = client_form.data.get('first_name')
    new_client.nickname = client_form.data.get('nickname')
    new_client.birth_date = client_form.data.get('birth_date')
    new_client.cpf = client_form.data.get('cpf')
    new_client.phone_number = client_form.data.get('phone_number')
    new_client.address = None

    if commit is True:
        new_client.save()

    return new_client
