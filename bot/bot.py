from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

import config

bot = Bot(token=config.bot.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Hello! 👋 I'm your tg bot.\n"
        "Use /help to get command list."
    )