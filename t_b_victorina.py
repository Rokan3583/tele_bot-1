import telebot

API_TOKEN = '7875467475:AAFkksGu0w2xW21HIVWH68cn7mNfvzVaWpE'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Вопросы и ответы для разных уровней сложности
easy_questions = [
    {
        'question': 'Какое животное является самым быстрым наземным животным?',
        'answers': ['Лев', 'Гепард', 'Антилопа'],
        'correct_answer': 'Гепард',
    },
    {
        'question': 'Какой хищник обитает в Арктике?',
        'answers': ['Белый медведь', 'Полярный волк', 'Оба этих ответа верны'],
        'correct_answer': 'Оба этих ответа верны',
    },
    {
        'question': 'Как называется детёныш слона?',
        'answers': ['Теленок', 'Щенок', 'Слонёнок'],
        'correct_answer': 'Слонёнок',
    }
]

medium_questions = [
    {
        'question': 'Какое животное считается символом мудрости?',
        'answers': ['Сова', 'Собака', 'Кошка'],
        'correct_answer': 'Сова',
    },
    {
        'question': 'Кто из этих животных имеет самый длинный хвост?',
        'answers': ['Жираф', 'Лиса', 'Ягуар'],
        'correct_answer': 'Жираф',
    },
    {
        'question': 'Какое животное способно менять окраску тела?',
        'answers': ['Хамелеон', 'Осьминог', 'Кальмар'],
        'correct_answer': 'Хамелеон',
    }
]

hard_questions = [
    {
        'question': 'У какого животного самая большая скорость полета?',
        'answers': ['Стриж', 'Беркут', 'Сапсан'],
        'correct_answer': 'Стриж',
    },
    {
        'question': 'Какое животное может спать до 20 часов в сутки?',
        'answers': ['Коала', 'Ленивец', 'Сурикат'],
        'correct_answer': 'Ленивец',
    },
    {
        'question': 'Какое животное обладает самым острым зрением среди млекопитающих?',
        'answers': ['Орёл', 'Сокол', 'Волк'],
        'correct_answer': 'Орёл',
    }
]

# Глобальные переменные для отслеживания состояния викторины
current_level = ''
current_questions = []
score = 0
current_question = None

# Клавиатуры для выбора уровня сложности и ответов
level_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
level_markup.row('Легкий', 'Средний')
level_markup.row('Сложный')

# Функция для начала игры
level_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
level_markup.row('Легкий', 'Средний')
level_markup.row('Сложный')

# Функция для начала игры
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}! Выбери уровень сложности:', reply_markup=level_markup)

# Обработка выбора уровня сложности
@bot.message_handler(regexp='^(Легкий|Средний|Сложный)$')
def choose_difficulty(message):
    global current_level, current_questions

    if message.text == 'Легкий':
        current_level = 'Легкий'
        current_questions = easy_questions.copy()
    elif message.text == 'Средний':
        current_level = 'Средний'
        current_questions = medium_questions.copy()
    elif message.text == 'Сложный':
        current_level = 'Сложный'
        current_questions = hard_questions.copy()

    ask_question(message)
def ask_question(message):
    global score, current_question

    # Если все вопросы пройдены, выводим результат
    if len(current_questions) == 0:
        bot.send_message(message.chat.id, f'Викторина завершена! Вы правильно ответили на {score} вопросов.')
        reset_game()
        return
def reset_game():
    global current_level, current_questions, score, current_question
    current_level = ''
    current_questions = []
    score = 0
    current_question = None

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки событий
    bot.polling()