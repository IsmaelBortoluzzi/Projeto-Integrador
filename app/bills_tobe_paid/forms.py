import datetime
from django import forms

from bills_tobe_paid.models import BillsToBePaid
from utils_global.translated_labels import bills_tobe_paid_labels


class BillsToBePaidForm(forms.ModelForm):

    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        initial=datetime.date.today,
        label='Due date'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = bills_tobe_paid_labels.get(value.label)

    class Meta:
        model = BillsToBePaid
        fields = ['entry_document', 'bill_type', 'installment_number', 'due_date', 'installment_value']
