import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update : Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Welcome To Our Quiz Bot")

async def help(update : Update , context: ContextTypes.DEFAULT_TYPE):
    help_message = """
    Available commands:
    - /start: Start the quiz or initiate the bot.
    - /help: Display the help message and provide information about available commands.
    - /generate_quiz: Generate a quiz based on a document.
    - /cancel: Cancel the current quiz and exit.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

async def generate_quiz(update : Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please send a PDF or DOCX file.")

async def cancel(update : Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Quiz canceled.")

if __name__ == '__main__':

    application    = ApplicationBuilder().token('TOKEN').build()
    start_handler  = CommandHandler('start', start)
    help_handler   = CommandHandler("help", help)
    quiz_handler   = CommandHandler("generate_quiz", generate_quiz)
    cancel_handler = CommandHandler("cancel", cancel)

    application.add_handler(start_handler)
    application.add_handler(quiz_handler)
    application.add_handler(help_handler)
    application.add_handler(cancel_handler)
    application.run_polling()


