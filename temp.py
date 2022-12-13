import requests
token = "5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk"
channel_name = '-1001808204758'
arr = {'Фио': 'Кабыкен Алмас',
       'Номер телефона': '87053876244',
       'Тема': 'Хата',
       'Сообщениеs': 'Помогите купить хату'}
txt = ''
# реализовываешь тут отправку данных в тг канал
for key, value in arr.items():
    txt += ''.join(key)
    txt += ''.join(' ' + value)
    txt += ''.join('\n')
url = f"https://api.telegram.org/bot5914175010:AAHGRNHJaeAyZmZNkGGAZRJNi0I28zw8Ebk/sendMessage?chat_id=-1001808204758&parse_mode=html&text={txt}"
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_name}&parse_mode=html&text={txt}"
print(requests.get(url).content)
