import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random
import json

from subprocess import Popen

TOKEN = ''
CHANNEL_ID = '@binbeginner'
NOT_SUB = 'Subscribe to this channel first'
ANOTHER_NOT_SUB = 'Subscription not found'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#return True if user is subscribed
def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False



Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
