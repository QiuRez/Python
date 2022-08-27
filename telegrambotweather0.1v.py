import telebot
import requests
import TokenWeather  # API Token для погоды
from tokenTelegramBot import TelegramToken  # АPI Token Telegram бота


#Телеграм Бог
bot = telebot.TeleBot(TelegramToken)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    respone = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + message.text + token)
    kelvin = respone.json()['main']['temp']
    celsiya = int(kelvin) - int(273)
    celsiya = str(celsiya)
    bot.send_message(message.chat.id, 'Температура: ' + celsiya)


bot.polling(none_stop=True, interval=0)
