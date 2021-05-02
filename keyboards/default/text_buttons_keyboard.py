from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

switchgear_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="КРУЭ-220кВ"),
            KeyboardButton(text="КРУЭ-110кВ"),
        ],
        [
            KeyboardButton(text="КРУ-10кВ блока №1"),
            KeyboardButton(text="КРУ-10кВ блока №2")
        ],
        [
            KeyboardButton(text="КРУ-10кВ СН"),
            KeyboardButton(text="КРУ-10кВ блока №3"),

        ],
        [
            KeyboardButton(text="КРУ-10кВ СН блока №3")
        ],


    ],
    resize_keyboard=True
)

element_220_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-220 Т-3"),
            KeyboardButton(text="ЭВ-220 КВЛ Дагомыс"),
        ],
        [
            KeyboardButton(text="ЭВ-220 Т-4"),
            KeyboardButton(text="ЭВ-220 КВЛ Псоу")
        ],
        [
            KeyboardButton(text="ЭВ-220 ШСЭВ"),
            KeyboardButton(text="ЭВ-220 АТ-1"),

        ],
        [
            KeyboardButton(text="ТН-220 1,2 СШ")
        ],
        [
            KeyboardButton(text="Назад"),
        ],

    ],
    resize_keyboard=True
)

element_110_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-110 ВЛ Бытха"),
            KeyboardButton(text="ЭВ-110 Т-5"),
        ],
        [
            KeyboardButton(text="ЭВ-110 ШСЭВ"),
            KeyboardButton(text="ЭВ-110 ВЛ Мацеста")
        ],
        [
            KeyboardButton(text="ЭВ-110 Т-1"),
            KeyboardButton(text="ЭВ-110 ВЛ Сочи I цепь"),

        ],
        [
            KeyboardButton(text="ЭВ-110 Т-2"),
            KeyboardButton(text="ЭВ-110 КВЛ Альпийская"),

        ],
        [
            KeyboardButton(text="ТН-110 1,2 СШ"),
            KeyboardButton(text="ЭВ-110 АТ-1"),

        ],
        [
            KeyboardButton(text="ЭВ-110 ВЛ Сочи II цепь"),
            KeyboardButton(text="ЭВ-110 КВЛ Хоста"),

        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

element_10_block1_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-10 ГТУ-1"),
            KeyboardButton(text="ЭВ-10 ПТУ-1"),
        ],
        [
            KeyboardButton(text="РПТ-10 Т-1"),
            KeyboardButton(text="РГТ-10 Т-1"),
        ],
        [
            KeyboardButton(text="ЭВ-10 Р-3")
        ],
        [
            KeyboardButton(text="Назад")
        ],

    ],
    resize_keyboard=True
)

element_10_block2_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-10 ГТУ-2"),
            KeyboardButton(text="ЭВ-10 ПТУ-2"),
        ],
        [
            KeyboardButton(text="РПТ-10 Т-2"),
            KeyboardButton(text="РГТ-10 Т-2"),
        ],
        [
            KeyboardButton(text="Назад")
        ],

    ],
    resize_keyboard=True
)

element_10_SN_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-10-1 Т-5"),
            KeyboardButton(text="ЭВ-10-2 Т-5"),
        ],
        [
            KeyboardButton(text="ТН-10 1СШ"),
            KeyboardButton(text="ТН-10 2СШ")
        ],
        [
            KeyboardButton(text="ЭВ-10 Р-1"),
            KeyboardButton(text="ЭВ-10 Р-2"),

        ],
        [
            KeyboardButton(text="ЭВ-10-1 ДГУ"),
            KeyboardButton(text="ЭВ-10-2 ДГУ"),

        ],
        [
            KeyboardButton(text="ЭВ-10 Р-4"),
        ],
        [
            KeyboardButton(text="Назад")
        ],

    ],
    resize_keyboard=True
)
element_10_block3_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ВВ-10 ГТУ-3"),
            KeyboardButton(text="ВВ-10 ГТУ-4"),
        ],
        [
            KeyboardButton(text="ТН-10-2 Т-3"),
            KeyboardButton(text="ТН-10-2 Т-4")
        ],
        [
            KeyboardButton(text="ВВ-10 Т-3"),
            KeyboardButton(text="ВВ-10 Т-4"),

        ],
        [
            KeyboardButton(text="ВВ-10 ПТУ-3"),
            KeyboardButton(text="ТН-10 3СШ"),

        ],
        [
            KeyboardButton(text="ВВ-10 Р-9"),
        ],
        [
            KeyboardButton(text="Назад")
        ],

    ],
    resize_keyboard=True
)

element_10_SN_block3_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ВВ-10-1 АТ-1"),
            KeyboardButton(text="ВВ-10-2 АТ-1"),
        ],
        [
            KeyboardButton(text="ТН-10 1СШ"),
            KeyboardButton(text="ТН-10 2СШ")
        ],
        [
            KeyboardButton(text="ВВ-10 Р-7"),
            KeyboardButton(text="ВВ-10 Р-8"),

        ],
        [
            KeyboardButton(text="ВВ-10 Р-5"),
            KeyboardButton(text="ВВ-10 Р-6"),

        ],
        [
            KeyboardButton(text="Назад")
        ],

    ],
    resize_keyboard=True
)

component_220_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-220"),
            KeyboardButton(text="ЗН ЭВ-220"),
        ],
        [
            KeyboardButton(text="ЛР(ТР)-220"),
            KeyboardButton(text="ЗН ЛР(ТР)-220")
        ],
        [
            KeyboardButton(text="ШР-220"),
            KeyboardButton(text="ЗН ШР-220"),

        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_110_line_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-110"),
            KeyboardButton(text="ЛР-110"),
        ],
        [
            KeyboardButton(text="ШР-110-1"),
            KeyboardButton(text="ШР-110-2"),
        ],
        [
            KeyboardButton(text="ЗН-110 ЭВ"),
            KeyboardButton(text="ЗН-110 ЛР")
        ],
        [
            KeyboardButton(text="ЗН-110 ШР"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_110_transformer_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-110"),
            KeyboardButton(text="ТР-110"),
        ],
        [
            KeyboardButton(text="ШР-110-1"),
            KeyboardButton(text="ШР-110-2"),
        ],
        [
            KeyboardButton(text="ЗН-110 ЭВ"),
            KeyboardButton(text="ЗН-110 ТР")
        ],
        [
            KeyboardButton(text="ЗН-110 ШР"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_110_buscoopler_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЭВ-110"),
        ],
        [
            KeyboardButton(text="ШР-110-1"),
            KeyboardButton(text="ШР-110-2"),
        ],
        [
            KeyboardButton(text="ЗН ШР-110-1"),
            KeyboardButton(text="ЗН ШР-110-2")
        ],
        [
            KeyboardButton(text="Назад"),
        ],

    ],
    resize_keyboard=True
)

component_110_VT_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ШР-110 1СШ"),
            KeyboardButton(text="ШР-110 2СШ"),
        ],
        [
            KeyboardButton(text="ЗН-110 ТН 1СШ"),
            KeyboardButton(text="ЗН-110 ТН 2СШ")
        ],
        [
            KeyboardButton(text="Назад"),
        ],

    ],
    resize_keyboard=True
)

component_10_gas_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тележка ЭВ-10"),
            KeyboardButton(text="ЗН ЭВ-10"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_10_vak_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тележка ВВ-10"),
            KeyboardButton(text="ЗН ВВ-10"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_10_rpt_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тележка РПТ-10"),
            KeyboardButton(text="ЗН РПТ-10"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_10_rgt_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тележка РГТ-10"),
            KeyboardButton(text="ЗН РГТ-10"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

component_10_tn_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ЗН ТН-10"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)


switchgear_status_ev = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нормальное условие работы"),
            KeyboardButton(text="Нормальное условие работы управление с дистанции"),
        ],
        [
            KeyboardButton(text="В ремонте"),
            KeyboardButton(text="С принудительной деблокировкой"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

switchgear_status_lr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нормальное условие работы"),
        ],
        [
            KeyboardButton(text="В ремонте"),
            KeyboardButton(text="С принудительной деблокировкой"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

switchgear_status_shr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нормальное условие работы"),
            KeyboardButton(text="При перефиксации"),
        ],
        [
            KeyboardButton(text="В ремонте"),
            KeyboardButton(text="С принудительной деблокировкой"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

switchgear_status_zn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нормальное условие работы"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)

switchgear_status_VT_zn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нормальное условие работы"),
            KeyboardButton(text="С принудительной деблокировкой"),
        ],
        [
            KeyboardButton(text="Назад"),

        ],

    ],
    resize_keyboard=True
)
