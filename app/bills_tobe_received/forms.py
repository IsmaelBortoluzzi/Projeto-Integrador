import datetime
from django import forms

from bills_tobe_received.models import BillsToBeReceived
from utils_global.translated_labels import bills_tobe_received_labels


class BillsToBeReceivedForm(forms.ModelForm):

    inclusion_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Data da inclusão', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = bills_tobe_received_labels.get(value.label)

    class Meta:
        model = BillsToBeReceived
        fields = ['remaining_value', 'order_id']
