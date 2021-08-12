import constants as keys
import responses1 as R
from telegram.ext import *

print('Bot started...')


def start_command(update, context):
    update.message.reply_text("Let's start!")


def help_command(update, context):
    update.message.reply_text("How can I help you?")


def handle_message(update, context):
    msg = str(update.message.text).lower()
    responses = R.sample_responses(msg)
    update.message.reply_text(responses)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API, use_context=True)
    d = updater.dispatcher

    d.add_handler(CommandHandler("start", start_command))
    d.add_handler(CommandHandler("help", help_command))
    d.add_handler(MessageHandler(Filters.text, handle_message))
    d.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()