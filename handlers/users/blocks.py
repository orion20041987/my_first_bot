from aiogram import types
from loader import dp, bot, db
from states import Blocks
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(text='/blocks')
async def operation_block_helper(message: types.Message):
    chat_id = message.chat.id
    user_name = message.chat.first_name
    await bot.send_message(chat_id=chat_id, text=f"Здравствуйте, {user_name}!\nУкажите, на какое распределительное"
                                                 f" устройство вам требуется подсказка? \n\n"
                                                 f"1. КРУЭ-220кВ\n"
                                                 f"2. КРУЭ-110кВ\n"
                                                 f"3. КРУ-10кВ блока №1\n"
                                                 f"4. КРУ-10кВ блока №2\n"
                                                 f"5. КРУ-10кВ блока №3\n"
                                                 f"6. КРУ-10кВ СН\n"
                                                 f"7. КРУ-10кВ СН блока №3\n\n"
                                                 f"или введите 'Q' чтобы выйти")
#
#     await Blocks.switchgear_choose.set()
#
#
# @dp.message_handler(state=Blocks.switchgear_choose)
# async def answer_switchgear_choose(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     async with state.proxy() as data:
#         data["answer_switchgear_choose"] = answer
#         print(data)
#
#     if data.get("answer_switchgear_choose") == "Q":
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text="Вы вышли из помошника по блокировкам.\n\n"
#                                                      "Для того, чтобы вернуться "
#                                                      "введите команду   'blocks' "
#                                                      "или воспользуйтесь меню быстрых комманд")
#         await state.reset_state()
#
#     elif data.get("answer_switchgear_choose") == "1":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ЭВ-220 Т-3\n"
#                                                      f"2. ЭВ-220 КВЛ Дагомыс\n"
#                                                      f"3. ЭВ-220 Т-4\n"
#                                                      f"4. ЭВ-220 КВЛ Псоу\n"
#                                                      f"5. ЭВ-220 ШСЭВ\n"
#                                                      f"6. ТН-220 1,2 СШ\n"
#                                                      f"7. ЭВ-220 АТ-1")
#         await Blocks.element_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "2":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ЭВ-110 ВЛ Бытха\n"
#                                                      f"2. ЭВ-110 Т-5\n"
#                                                      f"3. ЭВ-110 ШСЭВ\n"
#                                                      f"4. ЭВ-110 ВЛ Мацеста\n"
#                                                      f"5. ЭВ-110 Т-1\n"
#                                                      f"6. ЭВ-110 ВЛ Сочи I цепь\n"
#                                                      f"7. ЭВ-110 Т-2\n"
#                                                      f"8. ЭВ-110 КВЛ Альпийская\n"
#                                                      f"9. ТН-110 1,2 СШ\n"
#                                                      f"10. ЭВ-110 АТ-1 \n"
#                                                      f"11. ЭВ-110 ВЛ Сочи II цепь\n"
#                                                      f"12. ЭВ-110 КВЛ Хоста")
#         await Blocks.element_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "3":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ЭВ-10 ГТУ-1\n"
#                                                      f"2. ЭВ-10 ПТУ-1\n"
#                                                      f"3. ЭВ-10 ТСН-1\n"
#                                                      f"4. ЭВ-10 Р-3\n"
#                                                      f"5. РПТ-10 Т-1\n"
#                                                      f"6. РГТ-10 Т-1")
#         await Blocks.element_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "4":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ЭВ-10 ГТУ-2\n"
#                                                      f"2. ЭВ-10 ПТУ-2\n"
#                                                      f"3. ЭВ-10 ТСН-2\n"
#                                                      f"4. РПТ-10 Т-2\n"
#                                                      f"5. РГТ-10 Т-2")
#         await Blocks.element_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "5":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ЭВ-10 ГДК-1(2)\n"
#                                                      f"2. ЭВ-10 ЦН-1(2_3)\n"
#                                                      f"3. ЭВ-10-1(2) Т-5\n"
#                                                      f"4. ЭВ-10 ТСН-3\n"
#                                                      f"5. ЭВ-10 ТСН-4\n"
#                                                      f"6. ЭВ-10 ТСН-5\n"
#                                                      f"7. ЭВ-10 ТСН-6\n"
#                                                      f"8. ЭВ-10 ТЧЗН-1(2)\n"
#                                                      f"9. ТН-10 1(2)СШ\n"
#                                                      f"10. ЭВ-10 Р-1(2)\n"
#                                                      f"11. ЭВ-10-1(2) ДГУ\n"
#                                                      f"12. ЭВ-10 Р-4")
#         await Blocks.element_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "6":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ВВ-10 ГТУ-3(4)\n"
#                                                      f"2. ВВ-10 ТСН-7(8)\n"
#                                                      f"3. ТН-10-2 Т-3(4)\n"
#                                                      f"4. ТН-10 3СШ\n"
#                                                      f"5. ВВ-10 Т-3(4)\n"
#                                                      f"6. ВВ-10 ПТУ-3\n"
#                                                      f"7. ВВ-10 ТСН-12\n"
#                                                      f"8. ВВ-10 Р-9")
#         await Blocks.element_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "7":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, какая ячейка вас интересует? \n"
#                                                      f"1. ВВ-10-1(2) АТ-1\n"
#                                                      f"2. ТН-10 1(2)СШ\n"
#                                                      f"3. ВВ-10 ГДК-3(4)\n"
#                                                      f"4. ВВ-10 ТСН-9\n"
#                                                      f"5. ВВ-10 ТСН-10\n"
#                                                      f"6. ВВ-10 ТСН-11\n"
#                                                      f"7. ВВ-10 ТСН-12\n"
#                                                      f"8. ВВ-10 ТЧЗН-3(4)\n"
#                                                      f"9. ВВ-10 Р-7(8)\n"
#                                                      f"10. ВВ-10 Р-5(6)\n"
#                                                      f"11. ВВ-10 ЦН-4")
#         await Blocks.element_choose.set()
#
#
# @dp.message_handler(state=Blocks.element_choose)
# async def answer_switchgear_choose(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     async with state.proxy() as data:
#         data["answer_element_choose"] = answer
#         print(data)
#
#     if data.get("answer_element_choose") == "Q":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text="Вы вышли из помошника по блокировкам.\n\n"
#                                                      "Для того, чтобы вернуться "
#                                                      "введите команду   'blocks' "
#                                                      "или воспользуйтесь меню быстрых комманд")
#         await state.reset_state()
#
#     elif data.get("answer_switchgear_choose") == "1":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-220\n"
#                                                      f"2. ЗН ЭВ-220\n"
#                                                      f"3. ЛР(ТР)-220\n"
#                                                      f"4. ЗН ЛР(ТР)-220\n"
#                                                      f"5. ШР-220\n"
#                                                      f"6. ЗН ШР-220")
#         await Blocks.component_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "2":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-110\n"
#                                                      f"2. ЗН ЭВ-110\n"
#                                                      f"3. ЛР(ТР)-110\n"
#                                                      f"4. ЗН ЛР(ТР)-110\n"
#                                                      f"5. ШР-110\n"
#                                                      f"6. ЗН ШР-110")
#         await Blocks.component_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "3":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-10\n"
#                                                      f"2. ЗН ЭВ-10\n"
#                                                      f"3. Тележка ЭВ-10")
#         await Blocks.component_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "4":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-10\n"
#                                                      f"2. ЗН ЭВ-10\n"
#                                                      f"3. Тележка ЭВ-10")
#         await Blocks.component_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "5":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-10\n"
#                                                      f"2. ЗН ЭВ-10\n"
#                                                      f"3. Тележка ЭВ-10")
#         await Blocks.component_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "6":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-10\n"
#                                                      f"2. ЗН ЭВ-10\n"
#                                                      f"3. Тележка ЭВ-10")
#         await Blocks.component_choose.set()
#
#     elif data.get("answer_switchgear_choose") == "7":
#
#         chat_id = message.chat.id
#         await bot.send_message(chat_id=chat_id, text=f"Укажите, блокировка какого элемента вас интересует? \n"
#                                                      f"1. ЭВ-10\n"
#                                                      f"2. ЗН ЭВ-10\n"
#                                                      f"3. Тележка ЭВ-10")
#         await Blocks.component_choose.set()
#
#
# @dp.message_handler(state=Blocks.component_choose)
# async def answer_component_choose(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     async with state.proxy() as data:
#         await Blocks.select_blocking_conditions.set()
#         data["answer_component_choose"] = answer
#         print(data)
#
#         if data.get("answer_component_choose") == "Q":
#             chat_id = message.chat.id
#             await bot.send_message(chat_id=chat_id, text="Вы вышли из помошника по блокировкам.\n\n"
#                                                          "Для того, чтобы вернуться "
#                                                          "введите команду   'blocks' "
#                                                          "или воспользуйтесь меню быстрых комманд")
#             await state.reset_state()
#
#         selected_switchgear = data.get("answer_switchgear_choose")
#         selected_element = data.get("answer_element_choose")
#         selected_component = data.get("answer_component_choose")
#
#         chat_id = message.chat.id
#         try:
#             condition = db.select_blocking_condition(switchgear_id=f"{selected_switchgear}",
#                                                      element_id=f"{selected_element}",
#                                                      component_id=f"{selected_component}")
#             text = condition[0]
#
#         except Exception as e:
#             print(e)
#
#         await bot.send_message(chat_id=chat_id, text=text)
#         await state.reset_state(with_data=True)
