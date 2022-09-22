#!/usr/bin/env python3
# TODO: maybe an up command
import os
import telebot
from telebot.types import Message
from time import sleep
import requests

bot = telebot.TeleBot(os.environ['TELOXIDE_TOKEN'], parse_mode=None)

users = []
def usage():
    help_str = "Usage example:\n\n"
    help_str += "1./start https://github.com 30\n(sends request each 30 seconds)\n\n"
    help_str += "2./start https://github.com\n (sends request each 30 secs by default)"
    return help_str


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    bot.reply_to(message, usage(), disable_web_page_preview=True)


@bot.message_handler(commands=['count', 'length', 'len'])
def number_of_users(message: Message):
    bot.reply_to(message, f"Number of users: {len(users)}")

@bot.message_handler(commands=['start', 'up'])
def start_checking(message: Message):
    site = message.text.split()

    if len(site) <= 1:
        bot.reply_to(message, usage(), disable_web_page_preview=True)
        return
    else:
        timeout = int(site[2]) if len(site) == 3 else 30
        site = site[1]

    if message.from_user.id in users:
        bot.reply_to(message, "Already subscribed! BruhBot will notify if the site is down!")
        return
    else:
        users.append(message.from_user.id)

    bot.reply_to(message, f"Subscribed to the page!\nYou will be notified when the site goes down!")

    try:
        if requests.get(site).status_code != 200:
            bot.reply_to(message, "Site Down")
            users.clear()
            return
    except:
        bot.reply_to(message, "The provided site does not exist!")
        users.remove(message.from_user.id)
        return

    while 1:
        sleep(timeout)
        code: int = requests.get(site).status_code

        if code != 200:
            bot.reply_to(message, "Danger!!! Site down!!!")
            users.clear()

print("Starting the bot!")
bot.infinity_polling()
