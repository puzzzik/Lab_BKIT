from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    KeyboardButton

data = [
    "Я родився",
    "пойти в садик",
    "не пойду в сад(((",
    "пойти в школу",
    "идти в университет",
    "пойду в колледж",
    "на работку :(",
    "умереть.",
    "нет, умереть."
]

start = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
text = 'Я родився'
start.add(KeyboardButton(text=text))

text = "пойти в садик"
kindergarten = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=False, resize_keyboard=True)
kindergarten_btn_1 = KeyboardButton(text=text)
text = "не пойду в сад((("
kindergarten_btn_2 = KeyboardButton(text=text)
kindergarten.add(kindergarten_btn_1, kindergarten_btn_2)

school = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True).add(
    KeyboardButton(text='пойти в школу'))

uni = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uni1 = KeyboardButton(text='идти в университет')
uni2 = KeyboardButton(text='пойду в колледж')
uni.add(uni1, uni2)

work = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
work1 = KeyboardButton(text="на работку :(")

work2 = KeyboardButton(text='нет, умереть.')
work.add(work1, work2)

diebtn = KeyboardButton(text='умереть.')
die = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True).add(diebtn)
