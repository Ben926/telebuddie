import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def print_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    print(f"Chat ID: {chat.id}")
    await update.message.reply_text(f"Your chat ID is: {chat.id}")

if __name__ == "__main__":
    if not TOKEN:
        raise ValueError('TELEGRAM_BOT_TOKEN must be set in .env')
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, print_chat_id))
    print("Bot is running. Send a message to your bot in Telegram.")
    app.run_polling()
