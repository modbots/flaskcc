import logging
import random
import json
from subprocess import Popen

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."
Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)
if __name__ == "__main__":
    text = "LEEE ALL"
    print(echo(text))
