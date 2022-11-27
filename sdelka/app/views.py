from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
import urllib
from .forms import *


def index(req):
    items = reversed(Blog.objects.all())
    people = People.objects.all()
    return render(req, 'app/index.html', {'items': items, 'people': people})

class PeopleDetail(DetailView):
    model = People
    template_name = 'app/PeopleDetail.html'

class BlogDetail(DetailView):
    model = Blog
    template_name = 'app/BlogDetail.html'

def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            header = form.cleaned_data['header']
            message = form.cleaned_data['message']
            # bot_username = ''
            token = "5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk"
            channel_name = '@plussdelkainvite'
            arr = {'Фио': '421',
                   'Номер телефона': '421312',
                   'Тема': '321',
                   'Сообщениеs': '21'}
            txt = ''
            # реализовываешь тут отправку данных в тг канал
            for key, value in arr.items():
                txt += ''.join(key)
                txt += ''.join(' ' + value)
                txt += ''.join('\n')
            txt = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_name}&parse_mode=html&text={txt}"
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()

    return render(request, 'app/index.html', {'form': form})