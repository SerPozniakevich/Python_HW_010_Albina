from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime


def log(update: Update, context: CallbackContext,text):
    file = open('C:\\Users\\User\\Documents\\Geekbrains\\Python_HW\\Python_Tbot_calc_Albina\\db.csv', 'a')
    file.write(f'{datetime.now().strftime("%d.%m.%Y. %H:%M")}, {update._effective_user.first_name}, {update.effective_user.id}, {text}\n')
    file.close()