from django import forms
from googletrans import Translator

from product.models import Product
from product_entry_product.models import EntryProduct


class EntryProductModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        translator = Translator()
        labels = list()

        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})
            labels.append(value.label)

        string_to_translate = ' | '.join(labels)
        string_to_translate = translator.translate(string_to_translate, src='en', dest='pt').text
        string_to_translate = iter(string_to_translate.split(' |'))

        for key, value in self.fields.items():
            value.label = next(string_to_translate)

    class Meta:
        model = EntryProduct
        fields = '__all__'


class EntryProductForm(forms.Form):
    quantity = forms.IntegerField(required=True, label='Quantidade', min_value=1, max_value=2000000000)
    cost = forms.DecimalField(max_digits=7, decimal_places=2, required=False, label='Preço de custo')
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Produto')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cnpj').isdigit():
            raise forms.ValidationError('CNPJ deve conter somente dígitos!')

        return self.cleaned_data
