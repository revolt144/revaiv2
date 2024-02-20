import telebot

API_KEY = "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"

bot = telebot.TeleBot(6254933398:AAG8-z9LKy_H8hVYYWwfmMnxeHrNQr0CsdI)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /info \n /help \n /status")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Telegram bot created using the python-telegram-bot library.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running.")
    
print("Hey, I am up....")
bot.polling()
