import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("Hi Welcome")

def handle_message(update, context):
    if update.message.text == "bye":
        update.message.reply_text(f"you said {update.message.text}")
    elif update.message.text == "what is your name":
        update.message.reply_text("I am Alwin")
        update.message.make_as_read()

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()