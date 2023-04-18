import logging

from telegram.ext import Application

from opulus import settings
from services.commands import HANDLERS, error_handler

logger = logging.getLogger(__name__)


async def init(application: Application) -> None:
    await application.bot.set_my_commands(settings.MY_COMMANDS)


def main() -> None:
    application = Application.builder().token(settings.TOKEN).post_init(init).build()
    application.add_handlers(HANDLERS)
    application.add_error_handler(error_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
