from aiogram.dispatcher.filters.state import StatesGroup, State


class Blocks(StatesGroup):
    switchgear_choose = State()
    element_220_choose = State()
    element_110_choose = State()
    element_10_1_choose = State()
    element_10_2_choose = State()
    element_10_3_choose = State()
    element_10_SN_choose = State()
    element_10_3_SN_choose = State()
    component_220_choose = State()
    component_110_line_choose = State()
    component_110_transformer_choose = State()
    component_110_buscoopler_choose = State()
    component_110_VT_choose = State()
    component_10_1_choose = State()
    component_10_2_choose = State()
    component_10_3_choose = State()
    component_10_SN_choose = State()
    component_10_3_SN_choose = State()
    select_blocking_220_conditions = State()
    select_blocking_110_lr_conditions = State()
    select_blocking_110_shr_line_conditions = State()
    select_blocking_110_zn_TN_conditions = State()
    select_blocking_110_ev_conditions = State()
    select_blocking_110_shr_TN_conditions = State()
    select_blocking_110_zn_line_conditions = State()


class T(StatesGroup):
    name_input = State()
    email_input = State()
    sell_number_input = State()
