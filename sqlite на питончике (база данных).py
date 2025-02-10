import telebot
from telebot import types
bot = telebot.TeleBot('ваш токен')


#делаем чтобы бот при нажатии 'start' присылал стикер и текст.

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open ('sticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'добро пожаловать, <b> молодой человек </b>', parse_mode= "html")
    
# строки кода ниже, делают так, чтобы бот повторял сообщения.

@bot.message_handler(content_types=['text'])
def script(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
