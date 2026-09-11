import os

from dotenv import load_dotenv
from telegram import Bot


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def send_telegram_message(
    chat_id: int,
    message: str
):
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN not found in .env"
        )

    bot = Bot(
        token=TELEGRAM_BOT_TOKEN
    )

    await bot.send_message(
        chat_id=chat_id,
        text=message
    )   