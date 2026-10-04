import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your actual token from BotFather
TOKEN = 8682890615:AAFURo7eBIuPld1G3SKs19TH16hzFlC4jkU

# Set up basic logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Helper function to generate a signal
def get_random_signal():
    multiplier = round(random.uniform(1.20, 3.80), 2)
    confidence = random.randint(75, 98)
    return f"🚀 **AVIATOR SIGNAL ALERT**\n\n🎯 Target Multiplier: `{multiplier}x`\n🔥 Confidence: `{confidence}%`"

# Command: /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 **Welcome to the Aviator Signal Bot!**\n\n"
        "Use the following commands:\n"
        "• /signal - Get an instant signal\n"
        "• /stats - View today's performance stats\n"
        "• /help - Display instructions"
    )
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

# Command: /signal
async def signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal_msg = get_random_signal()
    await update.message.reply_text(signal_msg, parse_mode='Markdown')

# Command: /stats
async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wins = random.randint(18, 25)
    losses = random.randint(1, 4)
    win_rate = round((wins / (wins + losses)) * 100, 1)
    
    stats_text = (
        "📊 **TODAY'S BOT PERFORMANCE**\n\n"
        f"✅ Total Wins: `{wins}`\n"
        f"❌ Total Losses: `{losses}`\n"
        f"📈 Accuracy Rate: `{win_rate}%`"
    )
    await update.message.reply_text(stats_text, parse_mode='Markdown')

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "❓ **NEED HELP?**\n\n"
        "1. Click /signal to generate a signal manually.\n"
        "2. Click /stats to view performance accuracy.\n"
        "3. Make sure to react quickly when a signal drops!"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()

    # Register all command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("signal", signal_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
