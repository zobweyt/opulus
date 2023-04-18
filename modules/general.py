from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler

from opulus import settings


async def start_command(update: Update, _) -> None:
    message = "Я могу помочь облегчить ваши ежедневные задачи. " \
              "Ниже приведён список того, что я умею:\n\n"

    for command_info in settings.MY_COMMANDS:
        message += f"/{command_info.command} - {command_info.description}\n"
        
    await update.message.reply_text(message)


async def cancel_command(update: Update, _) -> int:
    await update.message.reply_text(
        "Выполнение текущей команды отменено.",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
