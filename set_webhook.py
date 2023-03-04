import requests
import os

url = 'https://pardayevsamandar.pythonanywhere.com/webhook'

TOKEN = os.environ["TOKEN"]

payload ={
    'url':url
}

r = requests.get('https://api.telegram.org/bot5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4/setWebhook',params=payload)

print(r.status_code)
# print(TOKEN)