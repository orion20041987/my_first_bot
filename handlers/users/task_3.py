import logging
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import task_3_callback
from keyboards.inline.tasks_keyboards import task_3_keyboard
from loader import dp


@dp.message_handler(Command("inline_buttons_1"))
async def task_3(message: types.Message):
    await message.answer(text="Edit @Sberleadbot info.\n\n"
                              "Name: Бот для Заданий на Курсе Udemy\n"
                              "Description: ?\n"
                              "About: ?\n"
                              "Botpic: ? no botpic\n"
                              "Commands: no commands yet", reply_markup=task_3_keyboard)
    print(f"пришло сообщение: '{message.text}'")


@dp.callback_query_handler(task_3_callback.filter(buttons_name="Edit Name"))
async def get_name(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f"callback_data = {call.data}")

    selected_button = callback_data["buttons_name"]
    print(f"В памяти {selected_button}")


@dp.callback_query_handler(task_3_callback.filter(buttons_name="Edit Description"))
async def get_description(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f"callback_data = {call.data}")

    selected_button = callback_data["buttons_name"]
    print(f"В памяти {selected_button}")


@dp.callback_query_handler(task_3_callback.filter(buttons_name="Edit About"))
async def get_about(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f"callback_data = {call.data}")

    selected_button = callback_data["buttons_name"]
    print(f"В памяти {selected_button}")


@dp.callback_query_handler(task_3_callback.filter(buttons_name="Edit Botpic"))
async def get_botpic(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f"callback_data = {call.data}")

    selected_button = callback_data["buttons_name"]
    print(f"В памяти {selected_button}")


@dp.callback_query_handler(task_3_callback.filter(buttons_name="Edit Commands"))
async def get_commands(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f"callback_data = {call.data}")

    selected_button = callback_data["buttons_name"]
    print(f"В памяти {selected_button}")


@dp.callback_query_handler(task_3_callback.filter(buttons_name="Back to Bot"))
async def get_back(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f"callback_data = {call.data}")

    selected_button = callback_data["buttons_name"]
    print(f"В памяти {selected_button}")
