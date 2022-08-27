import telebot
import requests
from weathertoken import tokenweather  # API Token для погоды
from tokenTelegramBot import TelegramToken  # АPI Token Telegram бота


#Телеграм Бог
bot = telebot.TeleBot(TelegramToken)


@bot.message_handler(commands=['start', 'help'])
def welcome_text(message):
    bot.send_message(
            message.chat.id, "Привет, друг!")
    bot.send_message(
            message.chat.id, "Введи название города, и я скажу температуру в нем")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    respone = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + message.text + tokenweather)
    kelvin = respone.json()['main']['temp']  # Температура
    country = respone.json()['sys']['country']  # Страна
    # Конвертация из градусов Кельвина в градусы Цельсия
    celsiya = int(kelvin) - int(273)
    celsiya = str(celsiya)
    bot.send_message(message.chat.id, "Температура: "
                     + celsiya
                     + "\nСтрана: "
                     + country
                     )


bot.polling(none_stop=True, interval=0)
