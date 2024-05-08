import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def start():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(start())
 