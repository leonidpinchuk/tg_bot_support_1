from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import K1_main_menu_reply, K2_reply, K3_reply, \
    main_menu

from main import bot, dp

from config import chat_id, start_message, \
    K1B1, K1B2, K1B3, K1B4, \
    K2K3K4_Back


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
    await message.answer('Выберите категорию, по которой Вы хотите оставить заявку в УК:', reply_markup=K2_reply)

@dp.message_handler(Text(equals=[K1B2]))
async def bot_start(message: Message):
    await message.answer('Выберите способ связи из нижеперечисленного списка:', reply_markup=K3_reply)

@dp.message_handler(Text(equals=[K1B2]))
async def bot_start(message: Message):
    await message.answer(START_MESSAGE_EN, reply_markup=main_menu)

@dp.message_handler(Text(equals=[K1B2]))
async def bot_start(message: Message):
    await message.answer(START_MESSAGE_EN, reply_markup=main_menu)

@dp.message_handler(Text(equals=[K2K3K4_Back]))
async def bot_start(message: Message):
    await message.answer(start_message, reply_markup=K1_main_menu_reply)

