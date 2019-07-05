# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
import socket
import socks
ip = '45.77.139.146'
port = 30762
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
socket.socket = socks.socksocket

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def inline(message):
    key = types.InlineKeyboardMarkup()
    But_Y = types.InlineKeyboardButton(text="Да", callback_data="Да")
    But_N = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
    But_W = types.InlineKeyboardButton(text="Warning", callback_data="Нет")
    key.add(But_Y, But_N,But_W)
    bot.send_message(message.chat.id, "Я прогер?", reply_markup=key)
    #bot.send_photo(message.chat.id, 'https://ibb.co/2WY9FnK');
    #bot.download_file(message.photo)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bobot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda Answer:True)
def inlin(Answer):
    if Answer.data == "Да":
        bot.send_message(Answer.message.chat.id, "Правильный ответ!")
    if Answer.data == "Нет":
        bot.send_message(Answer.message.chat.id, "Я ПРОГЕР!!!!!!!!!111!!!1!!!!")


@bot.message_handler(content_types=['photo'])
def photo(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

while True:
    try:
        bot.infinity_polling(True)
    except Exception as E:
        print(E.args)
        time.sleep(3)

