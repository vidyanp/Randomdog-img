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

u = Updater('1322478276:AAEK330uNreUm-1T5CFU8W0psjUl3opaCgw')
dp = u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
u.start_polling()
u.idle()
