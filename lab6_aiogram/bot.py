import config
from weather import Weather
import logging
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
w = Weather()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет!\nВ какой стране хотите узнать погоду?")
    #dbworker.set(message.chat.id, config.States.STATE_ENTER_COUNTRY.value)


@dp.message_handler(commands=['reset'])
async def reset(message):
    await message.answer("Начнем по новой! \nВ какой стране хотите узнать погоду?")
   # dbworker.set(message.chat.id, config.States.STATE_ENTER_COUNTRY.value)


# @dp.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_ENTER_COUNTRY.value)
# async def entering_country(message):
#     w.country = message.text
#    dbworker.set(message.chat.id, config.States.STATE_ENTER_CITY.value)
#     await message.answer("В каком городе хотите узнать погоду?")
#
#
# @dp.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_ENTER_CITY.value)
# async def entering_city(message):
#     w.city = message.text
#     dbworker.set(message.chat.id, config.States.STATE_SEND_WEATHER.value)
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     item = types.KeyboardButton('Показать погоду')
#     markup.add(item)
#     await message.answer('Нажмите, пожалуйста, на кнопку', reply_markup=markup)
#
# func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_SEND_WEATHER.value
@dp.message_handler(content_types=['text'])
async def sending_weather(message):
    resp = None
    #w.get_weather()
    if not resp:
        await message.answer('Повторите ввести данные заново\nТакого города или страны не существует')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item = types.KeyboardButton('Показать погоду')
        markup.add(item)
        await message.answer('Нажмите, пожалуйста, на кнопку', reply_markup=markup)
    else:
        await message.answer(resp)

   # dbworker.set(message.chat.id, config.States.STATE_ENTER_COUNTRY.value)
    await message.answer("В какой стране хотите узнать погоду?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)