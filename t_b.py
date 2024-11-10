import telebot

# Ваш токен от BotFather
API_TOKEN = '7873341111:AAF7_ysURMU0hSPfPNc-77NQ2G0FLHLOeO8'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, 'Привет! И тебе всего хорошего!!!!')

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки событий
    bot.polling()