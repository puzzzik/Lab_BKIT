import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import keyboards


class Form(StatesGroup):
    born = State()
    kindergarten = State()
    school = State()
    uni = State()
    work = State()
    death = State()


TOKEN = '5018239359:AAFC4dYuMLrxLzjIGJHaG8TXYdQbe1nrg0Y'

storage = MemoryStorage()
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Привет!\nЭто игра жизнь!")
    await message.answer("Начинаем?", reply_markup=keyboards.start)
    await Form.born.set()


@dp.message_handler(state='*', commands='reset')
@dp.message_handler(Text(equals='reset', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is not None:
        logging.info('Cancelling state %r', current_state)

    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.answer('Начнем по новой!', reply_markup=keyboards.start)
    await Form.born.set()


@dp.message_handler(lambda message: message.text not in keyboards.data, state='*')
async def wrong(message: types.Message, state: FSMContext):
    return await message.reply('Такого варианта нет\nПопробуйте ввести заново')


@dp.message_handler(state=Form.born)
async def born(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['born'] = "Родился!"

    await message.answer("Идти в садик?", reply_markup=keyboards.kindergarten)
    await Form.next()


@dp.message_handler(state=Form.kindergarten)
async def born(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['kindergarten'] = message.text

    await message.answer("Идти в школу?", reply_markup=keyboards.school)
    await Form.next()


@dp.message_handler(state=Form.school)
async def school(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['school'] = message.text

    await message.answer("Идти в ВУЗ?", reply_markup=keyboards.uni)
    await Form.next()


@dp.message_handler(state=Form.uni)
async def uni(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['uni'] = message.text

    await message.answer("Идти на работу?", reply_markup=keyboards.work)
    await Form.next()


@dp.message_handler(state=Form.work)
async def joby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['work'] = message.text
    await Form.next()
    if message.text == 'нет, умереть.':
        await Form.death.set()

    await message.answer("Ну все, пожили жизнь", reply_markup=keyboards.die)


@dp.message_handler(state=Form.death)
async def die(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['die'] = message.text
    await state.finish()

    await message.answer("Умерли.")

    await message.answer('Начнем по новой?', reply_markup=keyboards.start)
    await Form.born.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
