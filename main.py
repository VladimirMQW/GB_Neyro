import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

# Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Это бот для чата. Введи /help для справки"
    )


@dp.message(Command(commands=["stop"]))
async def start(message: types.Message):
    print(message.from_user.first_name)
    await message.answer(f"Пока, {message.chat.first_name}!")
    await bot.close()


@dp.message(Command(commands=["info"]))
async def send_info(message: types.Message):
    await message.answer(
        "Это простой телеграм бот и может ответить на несколько команд. Подробнее /help."
    )


@dp.message(Command(commands=["user"]))
async def send_user_info(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Ваше имя: {user.first_name}. Ваш id: {user.id}. Ваш username: @{user.username}"
    )


@dp.message(Command(commands=["help"]))
async def send_user_info(message: types.Message):
    user = message.from_user
    await message.answer(f"Бот понимает команды: /start, /stop, /info, /help, /user.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
