from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import K1B1, K1B2, K1B3, K1B4




main_menu_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=K1B1)
        ],
        [
            KeyboardButton(text=K1B2)
        ],
        [
            KeyboardButton(text=K1B3)
        ],
        [
            KeyboardButton(text=K1B4)
        ]
    ],
    resize_keyboard=True
)


main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Написать', url=CALL_LINK_RU)
        ]
    ]
)