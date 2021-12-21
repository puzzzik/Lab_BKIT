import os
import telebot
from telebot import types

TOKEN = '5017968274:AAFrEuyYMWEqUxpK6M59BDpbj_RE-wMoFsc'
# Сообщения
mes_hi = 'привет'
mes_whatsup = 'как дела?'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    text = message.text
    if text == mes_hi:
        bot.send_message(chat_id, 'Привет ✌️')
    elif text == mes_whatsup:
        img = open(os.path.join(cur_path, 'img', 'pic.jpg'), 'rb')
        bot.send_photo(message.from_user.id, img)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton(mes_hi)
        itembtn2 = types.KeyboardButton(mes_whatsup)
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)


bot.infinity_polling()