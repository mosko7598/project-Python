import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

# Load token .env file
load_dotenv()

# Create instances of Bot and Dispatcher
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Command /start handler
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}. Let's begin!")

# Echo message handler
@dp.message()
async def answer_as_echo(message: types.Message):
    try:
        await message.copy_to(message.chat.id)
    except Exception:
        await message.answer("Unsupported media type...")

# Main function
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

# Run the main function using asyncio
if __name__ == "__main__":
    asyncio.run(main())



