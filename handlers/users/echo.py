from aiogram import types
from loader import dp, bot


@dp.message_handler(text='/help')
async def bot_help(message: types.Message):
    text = message.text

    await message.reply(text)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    user_name = message.chat.first_name
    text = message.text

    await bot.send_message(chat_id=chat_id, text=text)
