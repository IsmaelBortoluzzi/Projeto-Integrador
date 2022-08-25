from order.models import Order


def create_new_order(order_form, commit=True):
    new_order = Order()

    new_order.selling_date = order_form.cleaned_data.get('selling_date')
    new_order.payment_form = order_form.cleaned_data.get('payment_form')
    new_order.is_active = order_form.cleaned_data.get('is_active')
    new_order.client_id = order_form.cleaned_data.get('client_id')

    if commit is True:
        new_order.save()


    return new_order
