from django.forms import ModelForm, TextInput

from .models import GrillReserve
from utils_global.translated_labels import grill_reserve_labels

class GrillReserveForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = grill_reserve_labels.get(value.label)

    class Meta:
        model = GrillReserve
        fields = '__all__'
        widgets = {
            'start_hour': TextInput(attrs={'type':'datetime-local'}),
            'finish_hour': TextInput(attrs={'type':'datetime-local'})
        }