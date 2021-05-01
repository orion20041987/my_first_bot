from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.storage import FSMContext

from keyboards.default import switchgear_choose, element_220_choose, element_110_choose, component_110_line_choose, \
    element_10_block1_choose, element_10_block2_choose, element_10_SN_choose, element_10_block3_choose, \
    element_10_SN_block3_choose, component_220_choose, component_10_gas_choose, component_10_rpt_choose, \
    component_10_rgt_choose, component_10_vak_choose, component_10_tn_choose, component_110_transformer_choose, \
    switchgear_status_ev, switchgear_status_shr, switchgear_status_lr, switchgear_status_zn, \
    component_110_buscoopler_choose, component_110_VT_choose, switchgear_status_VT_zn
from loader import dp, db, bot
from states import Blocks


@dp.message_handler(Command("tblocks"))
async def show_menu(message: types.Message):
    user_name = message.chat.first_name
    await message.answer(f"Здравствуйте, {user_name}!\nУкажите, на какое распределительное"
                         f" устройство вам требуется подсказка? \n\n"
                         , reply_markup=switchgear_choose)


@dp.message_handler(text="КРУЭ-220кВ")
async def get_220(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_220_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(text="КРУЭ-110кВ")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_110_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(text="КРУ-10кВ блока №1")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_10_block1_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(text="КРУ-10кВ блока №2")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_10_block2_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(text="КРУ-10кВ СН")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_10_SN_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(text="КРУ-10кВ блока №3")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_10_block3_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(text="КРУ-10кВ СН блока №3")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, какая ячейка вас интересует?", reply_markup=element_10_SN_block3_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_switchgear_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ЭВ-220 "]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_220_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ЭВ-110 ВЛ"]))
@dp.message_handler(Text(contains=["ЭВ-110 КВЛ"]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_110_line_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ЭВ-110 ШСЭВ"]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_110_buscoopler_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ТН-110 1,2 СШ"]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_110_VT_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ЭВ-110 Т"]))
@dp.message_handler(Text(contains=["ЭВ-110 АТ-1"]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_110_transformer_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ЭВ-10 "]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_10_gas_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ВВ-10 "]))
@dp.message_handler(Text(contains=["ВВ-10-"]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_10_vak_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["РПТ-10 "]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_10_rpt_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["РГТ-10 "]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_10_rgt_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(text="ТН-10 1СШ")
@dp.message_handler(text="ТН-10 2СШ")
@dp.message_handler(text="ТН-10-2 Т-3")
@dp.message_handler(text="ТН-10-2 Т-4")
@dp.message_handler(text="ТН-10 3СШ")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
                         reply_markup=component_10_tn_choose)
    answer = message.text

    async with state.proxy() as data:
        data["answer_element_choose"] = answer
        print(data)


@dp.message_handler(text="ЭВ-110")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_ev)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(text="ШР-110-1")
@dp.message_handler(text="ШР-110-2")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_shr)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(text="ЛР-110")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_lr)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(text="ЛР-110")
@dp.message_handler(text="ТР-110")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_lr)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(text="ЗН-110 ТН 1СШ")
@dp.message_handler(text="ЗН-110 ТН 2СШ")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_VT_zn)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(Text(contains=["ЗН-110 "]))
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_zn)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(text="ШР-110 1СШ")
@dp.message_handler(text="ШР-110 2СШ")
async def get_110(message: types.Message, state: FSMContext):
    await message.answer("Укажите, условия работыкоммутационного аппарата?",
                         reply_markup=switchgear_status_lr)
    answer = message.text

    async with state.proxy() as data:
        data["answer_component_choose"] = answer
        print(data)


@dp.message_handler(text="Нормальное условие работы")
@dp.message_handler(text="При перефиксации")
@dp.message_handler(text="В ремонте")
@dp.message_handler(text="С принудительной деблокировкой")
@dp.message_handler(text="Нормальное условие работы управление с дистанции")
async def get_110(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data["answer_status_choose"] = answer
        print(data)

    selected_switchgear = data.get("answer_switchgear_choose")
    selected_element = data.get("answer_element_choose")
    selected_component = data.get("answer_component_choose")
    selected_status = data.get("answer_status_choose")

    await message.answer(f"Поиск информации по элементу '{selected_component}', ячейки '{selected_element}', \
    '{selected_switchgear}'", reply_markup=ReplyKeyboardRemove())

    chat_id = message.chat.id
    try:
        condition = db.select_blocking_condition(switchgear_name=f"{selected_switchgear}",
                                                 element_name=f"{selected_element}",
                                                 component_name=f"{selected_component}",
                                                 switchgear_status=f"{selected_status}")
        text = condition[0]

        await bot.send_message(chat_id=chat_id, text=text)

    except Exception as e:
        print(e)

    await state.reset_state(with_data=True)


@dp.message_handler(text="ЗН ЭВ-10")
@dp.message_handler(text="Тележка ЭВ-10")
@dp.message_handler(text="ЗН ВВ-10")
@dp.message_handler(text="Тележка ВВ-10")
@dp.message_handler(text="Тележка РПТ-10")
@dp.message_handler(text="ЗН РПТ-10")
@dp.message_handler(text="Тележка РГТ-10")
@dp.message_handler(text="ЗН РГТ-10")
@dp.message_handler(text="ЗН ТН-10")
async def get_110(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data["answer_component_choose"] = answer
        print(data)

    selected_switchgear = data.get("answer_switchgear_choose")
    selected_element = data.get("answer_element_choose")
    selected_component = data.get("answer_component_choose")

    await message.answer(f"Поиск информации по элементу '{selected_component}', ячейки '{selected_element}', \
    '{selected_switchgear}'", reply_markup=ReplyKeyboardRemove())

    chat_id = message.chat.id
    try:
        condition = db.select_blocking_condition(switchgear_name=f"{selected_switchgear}",
                                                 element_name=f"{selected_element}",
                                                 component_name=f"{selected_component}")
        text = condition[0]

        await bot.send_message(chat_id=chat_id, text=text)

    except Exception as e:
        print(e)

    await state.reset_state(with_data=True)

# @dp.message_handler(Text(contains=["ЭВ-110 "]))
# async def get_110(message: types.Message, state: FSMContext):
#     await message.answer("Укажите, блокировка какого элемента ячейки вас интересует?",
#                          reply_markup=component_110_choose)
#     answer = message.text
#
#     async with state.proxy() as data:
#         data["answer_element_choose"] = answer
#         print(data)
#
#
# @dp.message_handler(text="КРУЭ-110кВ")
# async def get_110(message: types.Message):
#     await message.answer("Вы выбрали КРУЭ-110кВ")
#
#
# @dp.message_handler(Text(contains=["КРУ-10кВ"]))
# async def get_10(message: types.Message):
#     await message.answer(f'Вы выбрали: {message.text}', reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message_handler(text="КРУ-10кВ блока №1")
# async def get_10_1(message: types.Message):
#     await message.answer("Вы выбрали КРУ-10кВ блока №1")
#
#
# @dp.message_handler(text="КРУ-10кВ блока №2")
# async def get_10_2(message: types.Message):
#     await message.answer("Вы выбрали КРУ-10кВ блока №2")
#
#
# @dp.message_handler(text="КРУ-10кВ блока №3")
# async def get_10_3(message: types.Message):
#     await message.answer("Вы выбрали КРУ-10кВ блока №1")
#
#
# @dp.message_handler(text="КРУ-10кВ СН")
# async def get_10s(message: types.Message):
#     await message.answer("Вы выбрали КРУ-10кВ СН")
#
#
# @dp.message_handler(text="КРУ-10кВ СН блока №3")
# async def get_10s3(message: types.Message):
#     await message.answer("Вы выбрали КРУ-10кВ СН блока №3")
