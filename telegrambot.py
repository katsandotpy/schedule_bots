from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '6109872161:AAEGnoPlbSjftA8CKx9xS0Y8LIBnPTE6DJ4'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#команда start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я - робот долбоёб!")

#команда help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Для получения расписания введите 'дай расписание чмо' (без кавычек)")

#запрос расписания
@dp.message_handler()
async def file_message(msg: 'дай расписание чмо'):
    await msg.reply("Кому расписание, а кому хуев сосание, пошел нахуй")


#исполнение
if __name__ == '__main__':
    executor.start_polling(dp)