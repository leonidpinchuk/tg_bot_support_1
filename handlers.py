from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import K1_main_menu_reply, K2_reply, K3_reply, K4_reply, \
    call_me, drop_offer

from main import bot, dp

from config import chat_id, start_message, \
    K1B1, K1B2, K1B3, K1B4, \
    K2B1, K2B2, \
    K3B1, K3B2, \
    K2_message, K3_message, K4_message, K5_message, \
    K2K3K4_Back, \
    call_me_message, offer_message


async def send_hello(dp):
    ''' On startup '''
    await bot.send_message(chat_id=chat_id, text='Hello')

# Language (Выбор языка)
@dp.message_handler(Command('start'))
async def bot_start(message: Message):
    await message.answer(start_message, reply_markup=K1_main_menu_reply)

# K1
@dp.message_handler(Text(equals=[K1B1]))
async def bot_start(message: Message):
    await message.answer(K2_message, reply_markup=K2_reply)

@dp.message_handler(Text(equals=[K1B2]))
async def bot_start(message: Message):
    await message.answer(K3_message, reply_markup=K3_reply)

@dp.message_handler(Text(equals=[K1B3]))
async def bot_start(message: Message):
    await message.answer(K4_message, reply_markup=K4_reply)

@dp.message_handler(Text(equals=[K1B4]))
async def bot_start(message: Message):
    await message.answer(K5_message, reply_markup=K1_main_menu_reply)

@dp.message_handler(Text(equals=[K2K3K4_Back]))
async def bot_start(message: Message):
    await message.answer(start_message, reply_markup=K1_main_menu_reply)

# K2
@dp.message_handler(Text(equals=[K2B2]))
async def bot_start(message: Message):
    await message.answer(offer_message, reply_markup=drop_offer)

# K3
@dp.message_handler(Text(equals=[K3B1]))
async def bot_start(message: Message):
    await message.answer(call_me_message, reply_markup=call_me)


# K4


# K5


@dp.message_handler(Text(equals=['---']))
async def bot_start(message: Message):
    await message.answer('~!@#$%$#@!@#$%^%$#@!@$')





