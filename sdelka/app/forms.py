from django import forms
from .fields import ListTextWidget


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        headers = kwargs.pop('data_list', None)
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['header'].widget = ListTextWidget(data_list=headers, name='headers_list')

    name = forms.CharField(label='ФИО', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'ФИО :',
               'class': 'form-control'
               }
    ))
    number = forms.CharField(label='Номер телефона', max_length=12, widget=forms.TextInput(
        attrs={'placeholder': 'Номер телефона :',
               'class': 'form-control'
               }
    ))
    header = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs={'placeholder': 'Тема :',
               'class': 'form-control'
               }
    ))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение :',
               'class': 'form-control',
               'rows': '4'
               }
    ))


class HRForm(forms.Form):
    hr_number = forms.CharField(label='Номер телефона', max_length=12, widget=forms.TextInput(
        attrs={'placeholder': 'Номер телефона :',
               'class': 'rounded-pill'
               }
    ))