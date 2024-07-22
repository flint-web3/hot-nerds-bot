from settings import bot

@bot.message_handler(commands=['start'])
def start(message):
   bot.send_message( message.chat.id, 'The bot is under development. Wait for the news.', parse_mode="Markdown")

@bot.message_handler(content_types="text")
def new_mes(message):
   start(message)

if __name__ == '__main__':
   bot.infinity_polling()