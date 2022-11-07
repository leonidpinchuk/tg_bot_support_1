from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import




language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Русский')
        ],
        [
            KeyboardButton(text='English')
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