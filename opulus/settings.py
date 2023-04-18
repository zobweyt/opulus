import logging
import decouple

from telegram import BotCommand

LOG_FORMAT = "[%(asctime)s] %(levelname)s >> %(message)s"
LOG_DATEFMT = "%H:%M:%S"
LOG_LEVEL = logging.INFO

logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATEFMT, level=LOG_LEVEL)

TOKEN = decouple.config("TOKEN")

MY_COMMANDS = [
    BotCommand("start", "получить помощь по использованию бота"),
    BotCommand("weather", "получить текущую погоду в определённом месте"),
    BotCommand("cat", "прислать рандоиного котика"),
]

OWM_API_KEY = decouple.config("OWM_API_KEY")
