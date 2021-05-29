from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from states import T


@dp.message_handler(Command("form"))
async def name_ask(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text='Введите свое имя ')
    await T.name_input.set()


@dp.message_handler(state=T.name_input)
async def name_input(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    name = message.text
    async with state.proxy() as data:
        data['Name'] = name
        print(data)

    await bot.send_message(chat_id=chat_id, text='Введите свой e-mail ')
    await T.email_input.set()


@dp.message_handler(state=T.email_input)
async def email_input(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    email = message.text
    async with state.proxy() as data:
        data['email'] = email
        print(data)

    await bot.send_message(chat_id=chat_id, text='Введите свой номер телефона ')
    await T.sell_number_input.set()


@dp.message_handler(state=T.sell_number_input)
async def cell_number_input(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    cell_number = message.text
    async with state.proxy() as data:
        data['cell_number'] = cell_number
        print(data)

    name = data.get('Name')
    email = data.get('email')
    cell_number = data.get('cell_number')

    await bot.send_message(chat_id=chat_id, text=f'Привет! Ты ввел следующие данные:\n\n'
                                                 f'Имя - {name}\n\n'
                                                 f'Email - {email}\n\n'
                                                 f'Телефон: - {cell_number}')

    await state.reset_state(with_data=True)
