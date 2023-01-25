import logging
import random
import json
from subprocess import Popen

Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)




   
