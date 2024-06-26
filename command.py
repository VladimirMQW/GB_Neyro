import asyncio
import config
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command, CommandObject
import requests
from keyboards import keyboard

router = Router()


################### Команды ###############################
@router.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Это бот для чата. Введи /help для справки",
        reply_markup=keyboard,
    )


@router.message(Command(commands=["stop", "стоп"]))
async def stop(message: types.Message):
    print(message.from_user.first_name)
    await message.answer(f"Пока, {message.chat.first_name}!")
    await bot.close()


@router.message(Command(commands=["info", "инфо"]))
async def send_info(message: types.Message):
    await message.answer(
        "Это простой телеграм бот и может ответить на несколько команд. Подробнее /help.",
        reply_markup=keyboard,
    )


@router.message(Command(commands=["user"]))
async def send_user_info(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Ваше имя: {user.first_name}. Ваш id: {user.id}. Ваш username: @{user.username}"
    )


############ Погода #######################
@router.message(Command(commands=["weather"]))
async def get_weather(message: types.Message):
    msg = message.text.split(" ")
    # msg = message.split(" ")
    msg.remove(msg[0])
    msg = " ".join(msg)

    if not msg:
        await message.answer("Введи название города")
        return

    city = msg
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.token_ow}&units=metric&lang=ru"
    # await message.answer(f"Отладка {url}")
    response = requests.get(url)
    weather_data = response.json()

    # if weather_data.get("cod") == "404":
    #    await message.answer(f"Город {city} не найден.")
    #    return
    if weather_data["cod"] != 200:
        await message.answer(f"Город {city} не найден")
        return

    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    wind = weather_data["wind"]["speed"]
    await message.answer(
        f"Погода в городе {city}: Температура: {temperature}°C, Ветер: {wind} м/с, {description}"
    )


############ Погода ####################### end


@router.message(Command(commands=["help"]))
async def send_user_info(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Бот понимает команды: '/start', '/stop', '/info', '/help', '/user', '/quest', '/weather Наименование города'.\n И слова: привет, как дела, хорошо, пока"
    )
