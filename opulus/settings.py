import logging

from decouple import config
from telegram import BotCommand

LOG_FORMAT = "[%(asctime)s] %(levelname)s >> %(message)s"
LOG_DATEFMT = "%H:%M:%S"
LOG_LEVEL = logging.INFO

logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATEFMT, level=LOG_LEVEL)

TOKEN = config("TOKEN")

MY_COMMANDS = [
    BotCommand("start", "получить помощь по использованию бота"),
    BotCommand("weather", "получить текущую погоду в определённом месте"),
    BotCommand("cat", "прислать рандомного котика"),
    BotCommand("dog", "прислать рандомную собачку"),
]

OWM_API_KEY = config("OWM_API_KEY")
