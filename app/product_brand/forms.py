from django import forms

from product_brand.models import Brand
from utils_global.translated_labels import brand_labels

class BrandForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = brand_labels.get(value.label)

    class Meta:
        model = Brand
        fields = '__all__'