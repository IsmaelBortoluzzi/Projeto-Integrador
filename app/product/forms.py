from django import forms

from product.models import Product
from utils_global.translated_labels import product_labels

CATEGORY_CHOICES = (
    ('', 'Selecione a categoria'),
    ('Alimentos', 'Alimentos'),
    ('Bebidas', 'Bebidas'),
    ('Outros', 'Outros'),
)

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
        widgets = {
           'barcode': forms.NumberInput(attrs={'min': '1', 'step': '1'}),
           'selling_price': forms.NumberInput(attrs={'min': '0.01', 'step': '0.01'}),
           'profit_margin': forms.NumberInput(attrs={'min': '0.01', 'step': '0.01'}),
           'current_inventory': forms.NumberInput(attrs={'min': '1', 'step': '1'}),
           'minimum_inventory': forms.NumberInput(attrs={'min': '1', 'step': '1'}),
           'product_category': forms.Select(choices=CATEGORY_CHOICES,attrs={'class': 'form-control'}),
        }

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
        widgets = {
           'barcode': forms.NumberInput(attrs={'min': '1', 'step': '1'}),
           'selling_price': forms.NumberInput(attrs={'min': '0.01', 'step': '0.01'}),
           'profit_margin': forms.NumberInput(attrs={'min': '0.01', 'step': '0.01'}),
           'minimum_inventory': forms.NumberInput(attrs={'min': '1', 'step': '1'}),
           'product_category': forms.Select(choices=CATEGORY_CHOICES,attrs={'class': 'form-control'}),
        }
