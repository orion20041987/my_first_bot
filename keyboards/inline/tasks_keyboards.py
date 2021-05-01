from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import task_3_callback

task_3_keyboard = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(
                                                   text="Edit Name",
                                                   callback_data=task_3_callback.new(buttons_name="Edit Name")
                                               ),
                                               InlineKeyboardButton(
                                                   text="Edit Description",
                                                   callback_data=task_3_callback.new(buttons_name="Edit Description")
                                               ),
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="Edit About",
                                                   callback_data=task_3_callback.new(buttons_name="Edit About")
                                               ),
                                               InlineKeyboardButton(
                                                   text="Edit Botpic",
                                                   callback_data=task_3_callback.new(buttons_name="Edit Botpic")
                                               ),
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="Edit Commands",
                                                   callback_data=task_3_callback.new(buttons_name="Edit Commands")
                                               ),
                                               InlineKeyboardButton(
                                                   text="<<Back to Bot",
                                                   callback_data=task_3_callback.new(buttons_name="Back to Bot")
                                               ),
                                           ]

                                       ])
