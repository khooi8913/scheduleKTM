from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import stations
import trains
import bot_helper

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to MY_Traineer\n1. /train ORIGIN DESTINATION DATE\n2. /station STATE\n3. /state\n 4. /helper")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def helper(bot, update):
    str_help = 'IMPORTANT: How to retrieve schedule?\n\n'
    str_help += 'Step 1: /station to retrieve station code (e.g. /station WILAYAH PERSEKUTUAN)\n'
    str_help += 'Step 2: /train to get the schedule and availability (e.g. /station 19100 9000 03-SEP-2017)\n\n'
    str_help += 'More updates to come soon ... Conversation based query maybe?\n'
    bot.send_message(chat_id=update.message.chat_id, text=str_help)

def station(bot, update, args):
    STATE = ' '.join(str(state.upper()) for state in args)
    bot.send_message(chat_id=update.message.chat_id, text=bot_helper.list_station(STATE))

def train(bot, update, args):
    ORIGIN = args[0]
    DESTINATION = args[1]
    DATE = args[2]
    bot.send_message(chat_id=update.message.chat_id, text=bot_helper.list_train(ORIGIN, DESTINATION, DATE))

def state(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=bot_helper.list_of_states())

# YOUR TELEGRAM API PASSWORD HERE
updater = Updater(token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('helper', helper)
dispatcher.add_handler(help_handler)

station_handler = CommandHandler('station', station, pass_args=True)
dispatcher.add_handler(station_handler)

state_handler = CommandHandler('states', state)
dispatcher.add_handler(state_handler)

train_handler = CommandHandler('train', train, pass_args=True)
dispatcher.add_handler(train_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

def start_polling():
    updater.start_polling()

