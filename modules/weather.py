import random

from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
    Update,
)

from telegram.ext import ConversationHandler
from telegram.constants import ParseMode

from wallhaven.api import Wallhaven
from pyowm.commons.exceptions import NotFoundError

from services.owm import weather_manager, format_observation


LOCATION_REQUEST_STATE = range(1)


async def weather_command(update: Update, _) -> int:
    keyboard = [
        [KeyboardButton("Выбрать на карте", request_location=True)],
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Погоду в каком городе желаете получить?",
        reply_markup=markup
    )

    return LOCATION_REQUEST_STATE


async def send_weather(update: Update, _) -> int:
    try:
        if update.message.location:
            observation = weather_manager.weather_at_coords(
                update.message.location.latitude,
                update.message.location.longitude
            )
        else:
            observation = weather_manager.weather_at_place(update.message.text)
    except NotFoundError:
        await update.message.reply_text("Такого топонима не существует.")
        return LOCATION_REQUEST_STATE

    wallhaven = Wallhaven()

    # See more about the request params at https://wallhaven.cc/help/api.
    wallhaven.params["q"] = "nature weather"
    wallhaven.params["resolution"] = "1920x1080"
    wallhaven.params["sort"] = "relevance"

    response = wallhaven.search()

    image = random.choice(response.data).thumbs["large"]
    message = format_observation(observation)

    await update.message.reply_photo(
        image,
        message,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
