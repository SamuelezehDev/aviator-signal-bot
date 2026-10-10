import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace this with the token BotFather gave you
TOKEN = "8682890615:AAFURo7eBIuPld1G3SKs19TH16hzFlC4jkU"

# Configure logging to monitor activity in Render logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Aviator Signal Bot is active and running!")

def main() -> None:
    # Build application with token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Run polling loop
    print("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
