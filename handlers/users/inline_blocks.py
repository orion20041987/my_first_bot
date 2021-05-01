import logging
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import select_switchgear
from keyboards.inline.select_buttons import select_b, keyboard_220, keyboard_component_220
from loader import dp


@dp.message_handler(Command("inline"))
async def select_items(message: types.Message):
    user_name = message.chat.first_name
    await message.answer(text=f"Здравствуйте, {user_name}!\nУкажите, на какое распределительное"
                              f" устройство вам требуется подсказка? \n",
                         reply_markup=select_b)


@dp.callback_query_handler(select_switchgear.filter(item_name="select_220"))
async def get_220_i(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    await call.message.answer("Вы выбрали КРУЭ-220кВ", reply_markup=keyboard_220)

    selected_switchgear = callback_data["item_name"]
    print(f"В памяти {selected_switchgear}")


@dp.callback_query_handler(select_switchgear.filter(item_name="select_T3"))
async def get_T3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    await call.message.answer("Вы выбрали ЭВ-220кВ Т-3", reply_markup=keyboard_component_220)

    selected_element = callback_data["item_name"]
    print(f"В памяти {selected_element}")
