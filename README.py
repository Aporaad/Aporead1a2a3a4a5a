import telebot

# Create a bot object

bot = telebot.TeleBot("6228608379:AAGN6melXUYglRzvIv7tX9JyxKy_gCEyPwU")

# Define a function to handle incoming messages

def handle_message(message):

    # Get the message text

    text = message.text

    # If the message is "/start", send a welcome message

    if text == "/start":

        bot.send_message(message.chat.id, "Welcome to my bot!")

    # If the message is "/help", send a help message

    elif text == "/help":

        bot.send_message(message.chat.id, "Here are some commands you can use:")

        bot.send_message(message.chat.id, "/start - Start the bot")

        bot.send_message(message.chat.id, "/help - Get help")

    # Otherwise, reply with the message text

    else:

        bot.send_message(message.chat.id, text)

# Start the bot

bot.polling()
