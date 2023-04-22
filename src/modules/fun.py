from telegram import Update

from services.animals import Endpoints, get_random_animal_image_url


async def send_cat_command(update: Update, _) -> None:
    image = get_random_animal_image_url(Endpoints.CATS)
    await update.message.reply_photo(image)


async def send_dog_command(update: Update, _) -> None:
    image = get_random_animal_image_url(Endpoints.DOGS)
    await update.message.reply_photo(image)
