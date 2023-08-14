import os

import telebot

BOT_TOKEN = "6688067533:AAEE5RgXhQqVLTIfmD10HHn2t5aVYEC2eC8"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Halo " + message.text)

bot.infinity_polling()
