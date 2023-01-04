from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView
from .forms import *
import requests
def index(req):
    items = reversed(Blog.objects.all())
    people = People.objects.all()
    certificate = reversed(BonusCertificate.objects.all())
    organs = reversed(StateOrganPartner.objects.all())
    banks = reversed(BankPartner.objects.all())
    builders = reversed(BuilderPartner.objects.all())
    headers_list = 'Хотел бы продать квартиру', 'Хотел бы купить квартиру',\
                   'Не могли бы вы подобрать мне квартиру'

    context = {}
    if req.method == 'POST':
        contact_form = ContactForm(req.POST, data_list=headers_list)
        hr_form = HRForm(req.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            number = contact_form.cleaned_data['number']
            header = contact_form.cleaned_data['header']
            message = contact_form.cleaned_data['message']
            # bot_username = ''
            token = "5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk"
            channel_name = '-1001808204758'
            arr = {'Фио': name,
                   'Номер телефона': number,
                   'Тема': header,
                   'Сообщениеs': message}
            txt = ''
            # реализовываешь тут отправку данных в тг канал
            for key, value in arr.items():
                txt += ''.join(key)
                txt += ''.join(' ' + value)
                txt += ''.join('\n')
            contact_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_name}&parse_mode=html&text={txt}"
            print(requests.get(contact_url).content)
        if hr_form.is_valid():
            hr_number = hr_form.cleaned_data['hr_number']
            token = "5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk"
            channel_name = '-1001624941594'
            data = f'Номер телефона: {hr_number}'
            hr_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_name}&parse_mode=html&text={data}"
            print(requests.get(hr_url).content)
        return redirect('/')
    else:
        contact_form = ContactForm(data_list=headers_list)
        hr_form = HRForm()
    context  = {
        'contact_form': contact_form,
        'hr_form': hr_form,
        'items': items,
        'people': people,
        'certificate': certificate,
        'organs': organs,
        'banks': banks,
        'builders': builders,
    }
    return render(req, 'app/index.html', context)

def test(req):
    items = reversed(Estate.objects.all())
    context = {
        'items' : items,
    }
    return render(req, 'app/test.html', context)