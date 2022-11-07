from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import language

from main import bot, dp
from config import chat_id


async def send_hello(dp):
    ''' On startup '''
    await bot.send_message(chat_id=chat_id, text=HELLO)

# Language (Выбор языка)
@dp.message_handler(Command('start'))
async def bot_start(message: Message):
    await message.answer('Choose language/Выберите язык', reply_markup=language)

# Main_menu RU
@dp.message_handler(Text(equals=['Русский']))
async def bot_start(message: Message):
    await message.answer(START_MESSAGE_RU, reply_markup=main_menu_ru)

# Main_menu EN
@dp.message_handler(Text(equals=['English']))
async def bot_start(message: Message):
    await message.answer(START_MESSAGE_EN, reply_markup=main_menu_en)

