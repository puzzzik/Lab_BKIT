import os
import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5017968274:AAFrEuyYMWEqUxpK6M59BDpbj_RE-wMoFsc'
# Сообщения
mes_hi = 'привет'
mes_whatsup = 'как дела?'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types='text')
async def echo_all(message: types.Message):
    if message.text == mes_hi:
        await message.answer('Привет ✌️')
    elif message.text == mes_whatsup:
        img = open(os.path.join(cur_path, 'img', 'pic.jpg'), 'rb')
        await bot.send_photo(message.chat.id, img)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton(mes_hi)
        itembtn2 = types.KeyboardButton(mes_whatsup)
        markup.add(itembtn1, itembtn2)
        await message.answer('Пожалуйста, нажмите кнопку', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)