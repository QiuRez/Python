import telebot
import requests
import os
import random
import tgtocken
from telebot import types


sticker1 = open("C:\\Users\\QiuOp\\Desktop\\Python\\sticker.webp", "rb")
bot = telebot.TeleBot(tocken)
photo = []
s = 0
e = 0
vibor = []
file_name_sonya = []
file_name_egor = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🥰🥰Сонечка🥰🥰")
    btn2 = types.KeyboardButton("Егорик👻")
    markup.add(btn1, btn2)
    mesg = bot.send_message(message.chat.id, "Ты -", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if (message.text == "🥰🥰Сонечка🥰🥰"):
        sonya_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить рандом фото")
        sonya_markup.add(btn1)
        bot.send_message(message.chat.id, "Привет солнце😘")
        bot.send_sticker(message.chat.id, sticker1)
        bot.send_message(
            message.chat.id, "Отправь фотку, чтобы я её сохранил<3", reply_markup=sonya_markup)
        vibor.clear()
        vibor.append("Sonya")
    elif (message.text == "Егорик👻"):
        egor_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить рандом фото")
        egor_markup.add(btn1)
        bot.send_message(
            message.chat.id, "Отправь фотку своей женщине бездарь", reply_markup=egor_markup)
        vibor.clear()
        vibor.append("Egor")

    if (message.text == "Получить рандом фото" and vibor[0] == "Sonya"):
        answer = random.choice(file_name_egor)
        bot.send_photo(message.chat.id, open("C:\\Users\\QiuOp\\Desktop\\Python\\Egor\\" + answer, "rb"))
    elif (message.text == "Получить рандом фото" and vibor[0] == "Egor"):
        answer = random.choice(file_name_sonya)
        bot.send_photo(message.chat.id, open("C:\\Users\\QiuOp\\Desktop\\Python\\Sonya\\" + answer, "rb"))




@bot.message_handler(content_types=['photo'])
def save_photo(message):
    fileid = message.photo[-1].file_id
    file_info = bot.get_file(fileid)
    global s
    global e
    if (vibor[0] == "Sonya"):
        photo.clear()
        photo.append(fileid)
        if len(photo) == 1:
            send = bot.send_message(message.chat.id, "Фоточка пришла зайчик❤️")
            respone = requests.get(
                'https://api.telegram.org/file/bot' + tocken + "/" + file_info.file_path)
            with open("C:\\Users\\QiuOp\\Desktop\\Python\\Sonya\\" + "Photo_" + str(s) + ".jpg", "wb") as f:
                f.write(respone.content)
            file_name_sonya.append("Photo_" + str(s) + ".jpg")
            s = s + 1
    elif (vibor[0] == "Egor"):
        photo.clear()
        photo.append(fileid)
        if len(photo) == 1:
            send = bot.send_message(message.chat.id, "Фоточка пришла")
            respone = requests.get(
                'https://api.telegram.org/file/bot' + tocken + "/" + file_info.file_path)
            with open("C:\\Users\\QiuOp\\Desktop\\Python\\Egor\\" + "Photo_" + str(e) + ".jpg", "wb") as f:
                f.write(respone.content)
            file_name_egor.append("Photo_" + str(e) + ".jpg")
            e = e + 1


bot.polling(none_stop=True, interval=0)
