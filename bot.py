from flask import *
import requests
from subprocess import Popen

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."
Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)
Popen("python3 server/server.py", shell=True)
if __name__ == "__main__":
    text = "LEE PAR "
    print(text)
