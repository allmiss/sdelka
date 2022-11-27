from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=100)
    number = forms.CharField(label='Номер телефона', max_length=12)
    header = forms.CharField(label='Тема')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)