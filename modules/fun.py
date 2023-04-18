import enum
import requests

from telegram import Update


class Endpoints(enum.Enum):
    CATS = "https://api.thecatapi.com/v1/images/search"


async def send_cat_command(update: Update, _) -> None:
    image = requests.get(Endpoints.CATS.value).json()[0]["url"]
    await update.message.reply_photo(image)
