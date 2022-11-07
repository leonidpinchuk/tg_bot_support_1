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