import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "7710478380:AAHviSn0y1Jg8tdEeKGg5DLxhKZT24w7TZ8"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")

@dp.message(lambda message.photo)
async def photo_id(message: types.Message):
    await message.answer(message.photo[-1].photo_id)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())