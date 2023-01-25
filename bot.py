import logging
import random
import json
from subprocess import Popen
from aiogram import Bot, Dispatcher, executor, types



TOKEN = '5792941350:AAH-4wZamDd5UCseeJh5xDjiafKDs8SY2a9'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
