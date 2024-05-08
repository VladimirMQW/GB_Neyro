import asyncio
import config, command, msg, question, random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
import logging
import random
import requests

# from keyboards import keyboard
#################################################


################### Запуск
async def main():
    # Логирование
    logging.basicConfig(level=logging.INFO)
    #################################################
    # Объект бота и диспетчера
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_router(command.router)
    dp.include_router(question.router)
    dp.include_router(msg.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
