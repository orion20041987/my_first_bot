from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import select_switchgear, select_element, select_component

select_b = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[

                                    [
                                        InlineKeyboardButton(
                                            text="КРУЭ-220кВ",
                                            callback_data=select_switchgear.new(item_name="select_220")
                                        ),
                                        InlineKeyboardButton(
                                            text="КРУЭ-110кВ",
                                            callback_data=select_switchgear.new(item_name="select_110")
                                        ),

                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="КРУ-10кВ Блока №1",
                                            callback_data=select_switchgear.new(item_name="select_10_1")
                                        ),
                                        InlineKeyboardButton(
                                            text="КРУ-10кВ Блока №1",
                                            callback_data=select_switchgear.new(item_name="select_10_2")
                                        ),

                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="КРУ-10кВ Блока №3",
                                            callback_data=select_switchgear.new(item_name="select_10_3")
                                        ),
                                        InlineKeyboardButton(
                                            text="КРУ-10кВ СН",
                                            callback_data=select_switchgear.new(item_name="select_10_SN")
                                        ),

                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="КРУ-10кВ СН Блока №3",
                                            callback_data=select_switchgear.new(item_name="select_10_SN3")
                                        )

                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="Отмена",
                                            callback_data="cancel"
                                        )

                                    ]


                                ])

# keyboard_220 = InlineKeyboardMarkup()
#
# PEAR_LINK = "https://core.telegram.org/bots/api#inlinekeyboardmarkup"
# pear_link = InlineKeyboardButton(text="жми сюда!", url=PEAR_LINK)
#
# keyboard_220.insert(pear_link)

# keyboard_220 = InlineKeyboardMarkup(row_width=2,
#                                     inline_keyboard=[
#
#                                         [
#                                             InlineKeyboardButton(
#                                                 text="КРУЭ-220кВ",
#                                                 callback_data=select_switchgear.new(item_name="select_220")
#                                             ),
#                                             InlineKeyboardButton(
#                                                 text="КРУЭ-110кВ",
#                                                 callback_data=select_switchgear.new(item_name="select_110")
#                                             ),
#
#                                         ]
#                                     ])



keyboard_220 = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[

                                        [
                                            InlineKeyboardButton(
                                                text="ЭВ-220 Т-3",
                                                callback_data=select_element.new(item_name="select_T3")
                                            ),
                                            InlineKeyboardButton(
                                                text="ЭВ-220 КВЛ Дагомыс",
                                                callback_data=select_element.new(item_name="select_Dagomys")
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="ЭВ-220 Т-4",
                                                callback_data=select_element.new(item_name="select_T4")
                                            ),
                                            InlineKeyboardButton(
                                                text="ЭВ-220 КВЛ Псоу",
                                                callback_data=select_element.new(item_name="select_Psou")
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="ЭВ-220 ШСЭВ-220",
                                                callback_data=select_element.new(item_name="select_buscupler")
                                            ),
                                            InlineKeyboardButton(
                                                text="ЭВ-220 АТ-1",
                                                callback_data=select_element.new(item_name="select_AT1")
                                            ),
                                        ],

                                    ])

keyboard_component_220 = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[

                                        [
                                            InlineKeyboardButton(
                                                text="ЭВ-220",
                                                callback_data=select_component.new(item_name="select_EV")
                                            ),
                                            InlineKeyboardButton(
                                                text="ЗН ЭВ-220",
                                                callback_data=select_component.new(item_name="select_ZNEV")
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="ЛР(ТР)-220",
                                                callback_data=select_component.new(item_name="select_LR")
                                            ),
                                            InlineKeyboardButton(
                                                text="ЗН ЛР(ТР)-220",
                                                callback_data=select_component.new(item_name="select_ZNLR")
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="ШР-220",
                                                callback_data=select_component.new(item_name="select_SHR")
                                            ),
                                            InlineKeyboardButton(
                                                text="ЗН ШР-220",
                                                callback_data=select_component.new(item_name="select_ZNSHR")
                                            ),
                                        ],

                                    ])