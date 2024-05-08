import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def process_start_message(message: types.Message):
  """Приветствие"""
  await message.answer('Привет!')
  logging.debug('Привет!')


@dp.message()
async def echo(message: types.Message):
  """Эхо-ответ"""
  await message.answer(message.text)
  
async def start():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(start())
 