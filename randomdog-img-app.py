import os
from Adafruit_IO import Client
from telegram.ext import Updater,CommandHandler
import requests #getting the data from the cloud

def get_url():
  conents = requests.get('https://random.dog/woof.json').json()
  url = conents['url']
  return url

def dog(bot,update):
  url = get_url()
  chat_id = update.message.chat_id
  bot.send_photo(chat_id,photo=url)

  ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
API = os.getenv('API')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
u =Updater(API,use_context=True)

dp = u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
u.start_polling()
u.idle()

