from aiogram import Bot, Dispatcher, executer, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN = "6008739161:AAGwGUt9HoD2RoM7_MjabaZOtByFECN6JHE"

bot =  Bot(token=Token)

db = Dispatcher(bot=bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)

@dp.message_handler(commands=['start'])
async def start_command(mesage: types.Message):
    await message.reply(text="Qalaysan Tursunxon")
# @dp.message_handler()
# async def echo_answer(message: types.Message):
#     avait message.answer(text=message.text.upper())\
@dp.message_handler(Text(equals="commands"))
async def get_commands(message: types.Message):
   text = """
        /start - create a new bot
        /start - edit your bots [beta]

    await message.answer(text=text)

if __name__ == '__main__':
    executer.start_polling(dispatcher=db)

