import config
import telebot
import dbworker
from weather import Weather
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
w = Weather()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет!\nВ какой стране хотите узнать погоду?")
    dbworker.set(message.chat.id, config.States.STATE_ENTER_COUNTRY.value)


@bot.message_handler(commands=['reset'])
def reset(message):
    bot.send_message(message.chat.id, "Начнем по новой! \nВ какой стране хотите узнать погоду?")
    dbworker.set(message.chat.id, config.States.STATE_ENTER_COUNTRY.value)


@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_ENTER_COUNTRY.value)
def entering_country(message):
    w.country = message.text
    dbworker.set(message.chat.id, config.States.STATE_ENTER_CITY.value)
    bot.send_message(message.chat.id, "В каком городе хотите узнать погоду?")


@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_ENTER_CITY.value)
def entering_city(message):
    w.city = message.text
    dbworker.set(message.chat.id, config.States.STATE_SEND_WEATHER.value)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item = types.KeyboardButton('Показать погоду')
    markup.add(item)
    bot.send_message(message.chat.id, 'Нажмите, пожалуйста, на кнопку', reply_markup=markup)


@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_SEND_WEATHER.value)
def sending_weather(message):
    resp = w.get_weather()
    if not resp:
        bot.send_message(message.chat.id, 'Повторите ввести данные заново\nТакого города или страны не существует')
    else:
        bot.send_message(message.chat.id, resp)
    dbworker.set(message.chat.id, config.States.STATE_ENTER_COUNTRY.value)
    bot.send_message(message.chat.id, "В какой стране хотите узнать погоду?")


if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
