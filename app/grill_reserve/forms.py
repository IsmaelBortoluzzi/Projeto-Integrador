from django import forms

from .models import GrillReserve
from googletrans import Translator


class GrillReserveForm(forms.ModelForm):

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
        model = GrillReserve
        fields = '__all__'