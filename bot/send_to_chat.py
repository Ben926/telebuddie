
import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

if not TOKEN or not CHAT_ID:
    raise ValueError('TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in .env')

bot = Bot(token=TOKEN)

async def send_message(text: str, chat_id: str = None):
    """
    Send a message to the specified chat_id (defaults to env CHAT_ID).
    Usage:
        from send_to_group import send_message
        asyncio.run(send_message("Hello!"))
    """
    target_id = chat_id or CHAT_ID
    await bot.send_message(chat_id=target_id, text=text)

def send_to_chat(text: str, chat_id: str = None):
    asyncio.run(send_message(text, chat_id))
    