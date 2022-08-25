from django import forms

from product.models import Product
from order.models import Order
from .models import ProductOutput
from utils_global.translated_labels import product_output_labels

class ProductOutputModelForm(forms.ModelForm):

    order = forms.ModelChoiceField(queryset=Order.objects.all().filter(is_active=True).order_by('id'), label='Order', required=True)
    product_id = forms.ModelChoiceField(queryset=Product.objects.all().order_by('id'), label='Product id', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = product_output_labels.get(value.label)

    class Meta:
        model = ProductOutput
        fields = ['order', 'product_id', 'sold_price', 'quantity']

