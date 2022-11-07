from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import main_menu_reply, main_menu

from main import bot, dp

from config import chat_id, \
    K1B1, K1B2, K1B3, K1B4


async def send_hello(dp):
    ''' On startup '''
    await bot.send_message(chat_id=chat_id, text=HELLO)

# Language (Выбор языка)
@dp.message_handler(Command('start'))
async def bot_start(message: Message):
    await message.answer('Choose language/Выберите язык', reply_markup=main_menu_reply)

# Main_menu RU
@dp.message_handler(Text(equals=[K1B1]))
async def bot_start(message: Message):
    await message.answer(START_MESSAGE_RU, reply_markup=main_menu)

# Main_menu EN
@dp.message_handler(Text(equals=['English']))
async def bot_start(message: Message):
    await message.answer(START_MESSAGE_EN, reply_markup=main_menu)

