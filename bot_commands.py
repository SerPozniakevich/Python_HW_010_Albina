from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *

operation = 0
operands = []


def help_command(update: Update, context: CallbackContext):
    global operation
    operation = 0

    res_str =""
    res_str += 'Программа Калькулятор\n'
    res_str += 'Выберете действие и введите операнды:\n'
    res_str += 'Сложение /sum\n'
    res_str += 'Вычытание /sub\n'
    res_str += 'Умножение /mul\n'
    res_str += 'Деление /div\n'
    res_str += 'Возведение в степень /deg\n'
    res_str += 'Комплексное число следует вводить через пробел Real Imag'
    update.message.reply_text(res_str)


def sum_command(update: Update, context: CallbackContext):
    global operation
    operation = 1   

def sub_command(update: Update, context: CallbackContext):
    global operation
    operation = 2

def mul_command(update: Update, context: CallbackContext):
    global operation
    operation = 3

def div_command(update: Update, context: CallbackContext):
    global operation
    operation = 4

def deg_command(update: Update, context: CallbackContext):
    global operation
    operation = 5


def analize_command(update: Update, context: CallbackContext):
    global operation, operands
    res_str = ""

    if operation:
        if len(operands) < 2:
            msg = update.message.text

            if " " in msg and msg.split(" ")[0].isdigit() and msg.split(" ")[1].isdigit():
                operands.append(complex(float(msg.split(" ")[0]), float(msg.split(" ")[1])))
                update.message.reply_text(f'Комплексное число {operands[-1]}')
            elif msg.isdigit():
                operands.append(float(msg))
            else:
                update.message.reply_text(f'Вы ввлели не число, повторите ввод') 
        if len(operands) == 2:
            match operation:
                case 1:
                    res_str = f'{operands[0]} + {operands[1]} = {operands[0] + operands[1]}'
                case 2:
                    res_str = f'{operands[0]} - {operands[1]} = {operands[0] - operands[1]}'
                case 3:
                    res_str = f'{operands[0]} * {operands[1]} = {operands[0] * operands[1]}'
                case 4:
                    res_str = f'{operands[0]} : {operands[1]} = {operands[0] / operands[1]}'
                case 5:
                    res_str = f'{operands[0]} в степени {operands[1]} = {operands[0] ** operands[1]}'
            log(update,context,res_str)
            res_str += '\nПосчитаем ещё? /help'
            update.message.reply_text(res_str)
            operation = 0
            operands = []
