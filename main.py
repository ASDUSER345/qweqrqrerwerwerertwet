import os
from background import keep_alive #импорт функции для поддержки работоспособности
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time

bot = telebot.TeleBot('7177098010:AAG13xPn3T0EeV94HEzQl9m0fOj7syXObU4')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  bot.send_message(message.from_user.id,message.text)
# echo-функция, которая отвечает на любое текстовое сообщение таким же текстом   

keep_alive()#запускаем flask-сервер в отдельном потоке. Подробнее ниже...
bot.polling(non_stop=True, interval=0) #запуск бота