from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import K1B1, K1B2, K1B3, K1B4, \
    K2B1, K2B2, \
    K3B1, K3B2, \
    K4B1, K4B2, \
    K2K3K4_Back


# K1
K1_main_menu_reply = ReplyKeyboardMarkup(
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

# K2
K2_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=K2B1)
        ],
        [
            KeyboardButton(text=K2B2)
        ],
        [
            KeyboardButton(text=K2K3K4_Back)
        ],
        [
            KeyboardButton(text='---')
        ]
    ],
    resize_keyboard=True
)

# K3
K3_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=K3B1)
        ],
        [
            KeyboardButton(text=K3B2)
        ],
        [
            KeyboardButton(text=K2K3K4_Back)
        ],
        [
            KeyboardButton(text='---')
        ]
    ],
    resize_keyboard=True
)

# K4
K4_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=K4B1)
        ],
        [
            KeyboardButton(text=K4B2)
        ],
        [
            KeyboardButton(text=K2K3K4_Back)
        ],
        [
            KeyboardButton(text='---')
        ]
    ],
    resize_keyboard=True
)




call_me = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Да', url='google.com')
        ],
        [
            InlineKeyboardButton('Оставить номер телефона', url='google.com')
        ]
    ]
)