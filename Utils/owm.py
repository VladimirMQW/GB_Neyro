import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import config


# Функция для получения погоды
def get_weather(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Пожалуйста, укажите город.")
        return

    city = context.args[0]  # Получаем название города из сообщения пользователя
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}&units=metric&lang=ru"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get("cod") == "404":
        update.message.reply_text(f"Город {city} не найден.")
        return

    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    update.message.reply_text(
        f"Погода в {city}: Температура: {temperature}°C, {description}"
    )


def fox():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        image = data.get("image")
        return image


if __name__ == "__main__":
    print(fox())
