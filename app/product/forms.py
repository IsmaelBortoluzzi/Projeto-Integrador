from django import forms

from product.models import Product
from utils_global.translated_labels import product_labels


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = product_labels.get(value.label)

    class Meta:
        model = Product
        fields = [
                'name', 'barcode', 'selling_price', 'brand', 'product_category',
                'description', 'profit_margin', 'current_inventory','minimum_inventory'
            ]

class ProductEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = product_labels.get(value.label)

    class Meta:
        model = Product
        fields = [
                'is_active', 'name', 'barcode', 'selling_price', 'brand', 'product_category',
                'description', 'profit_margin', 'minimum_inventory'
            ]
