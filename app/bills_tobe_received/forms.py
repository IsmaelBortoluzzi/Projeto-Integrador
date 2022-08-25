import datetime
from django import forms

from bills_tobe_received.models import BillsToBeReceived
from order.models import Order
from utils_global.translated_labels import bills_tobe_received_labels


class BillsToBeReceivedForm(forms.ModelForm):

    inclusion_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Inclusion date', required=False)
    order_id = forms.ModelChoiceField(queryset=Order.objects.all().filter(is_active=True).order_by('id'), label='Order id', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = bills_tobe_received_labels.get(value.label)

    class Meta:
        model = BillsToBeReceived
        fields = ['order_id', 'remaining_value', 'inclusion_date']
