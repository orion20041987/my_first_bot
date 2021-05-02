from aiogram.dispatcher.filters.state import StatesGroup, State


class Blocks(StatesGroup):
    switchgear_choose = State()
    element_choose = State()
    component_choose = State()
    select_blocking_conditions = State()


class T(StatesGroup):
    name_input = State()
    email_input = State()
    sell_number_input = State()
