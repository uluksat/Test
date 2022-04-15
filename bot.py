from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot=Bot(token="5398933999:AAEgPoXqSwTSUiJUZjMisC2f-7wGHxGQZm4")
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет мир")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я эхо бот")

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id,message.text)

if __name__=='__main__':
    executor.start_polling(dp)




