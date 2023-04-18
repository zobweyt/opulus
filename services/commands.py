import logging

from telegram import Update

from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from modules import general, fun, weather

logger = logging.getLogger(__name__)

FALLBACKS = [
    CommandHandler("cancel", general.cancel_command),
]

HANDLERS = (
    CommandHandler("start", general.start_command),
    CommandHandler("cat", fun.send_cat_command),
    ConversationHandler(
        entry_points=[CommandHandler("weather", weather.weather_command)],
        states={
            weather.LOCATION_REQUEST_STATE: [
                MessageHandler(
                    filters.LOCATION | (filters.TEXT & ~filters.COMMAND),
                    weather.send_weather
                ),
            ],
        },
        fallbacks=FALLBACKS
    ),
    MessageHandler(filters.TEXT & ~filters.COMMAND, general.start_command),
)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Exception while handling an update:", exc_info=context.error)

    await update.message.reply_text(
        "Упс! Что-то пошло не так...\n"
        "Повторите попытку позже."
    )
