import logging
from aiogram import Bot, Dispatcher, executor, types

import random
import json

from subprocess import Popen



Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
