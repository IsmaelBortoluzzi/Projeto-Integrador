from client.models import Client
from order.models import Order
from product.models import Product
from product_output.models import ProductOutput


def create_order_with_one_product(order_product, commit=True):
    new_order = Order()
    new_output_product = ProductOutput()

    new_order.selling_date = order_product.cleaned_data.get('selling_date')
    new_order.payment_form = order_product.cleaned_data.get('payment_form')
    new_order.is_active = order_product.cleaned_data.get('is_active')
    new_order.client_id = order_product.cleaned_data.get('client_id')
    new_order.supplier = order_product.cleaned_data.get('supplier')

    new_output_product.quantity = order_product.cleaned_data.get('quantity')
    new_output_product.product_id = order_product.cleaned_data.get('product')

    if commit is True:
        new_order.save()

        new_output_product.order = new_order
        new_output_product.save()

    return new_order, new_output_product
