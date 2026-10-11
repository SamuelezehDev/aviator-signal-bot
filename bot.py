import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace this with the token BotFather gave you
TOKEN = "8682890615:AAFURo7eBIuPld1G3SKs19TH16hzFlC4jkU"

# Configure logging to monitor activity in your deployment logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    welcome_message = (
        f"Hello {user_name}! Welcome to the Aviator Signal Bot ✈️\n\n"
        "Use /signal to generate the latest predicted multiplier, or /help to see all options."
    )
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "🤖 **Aviator Bot Commands:**\n\n"
        "/start - Start the bot\n"
        "/signal - Get a new Aviator multiplier prediction\n"
        "/help - Show this help menu"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Generate a random multiplier for simulation (e.g., between 1.10x and 9.50x)
    multiplier = round(random.uniform(1.10, 9.50), 2)
    
    # Assign risk levels based on the multiplier
    if multiplier < 2.0:
        status = "🟡 Low Risk / Cash out early"
    elif multiplier < 5.0:
        status = "🟢 Moderate Risk / Good target"
    else:
        status = "🔥 High Risk / High Multiplier!"

    signal_text = (
        f"✈️ **Aviator Signal Generated:**\n\n"
        f"🎯 Target Multiplier: **{multiplier}x**\n"
        f"📊 Analysis: {status}\n\n"
        f"⚠️ *Play responsibly!* "
    )
    await update.message.reply_text(signal_text, parse_mode="Markdown")

def main() -> None:
    # Build the application using your token
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("signal", signal_command))

    # Start the bot
    logger.info("Aviator Bot is starting up and ready for polling...")
    application.run_polling()

if __name__ == "__main__":
    main()
