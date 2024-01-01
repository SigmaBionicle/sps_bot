import telebot
from telebot import types

API_TOKEN = '...'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Чтобы подать заявку, введите название проекта:")
    bot.register_next_step_handler(message, process_project_name_step)


def process_project_name_step(message):
    # сохраняем ответ пользователя в качестве названия проекта
    chat_id = message.chat.id
    project_name = message.text

    bot.send_message(chat_id, "Введите описание проекта:")
    bot.register_next_step_handler(message, process_project_description_step, project_name)


def process_project_description_step(message, project_name):
    # сохраняем описание проекта и просим выбрать исполнителя
    chat_id = message.chat.id
    project_description = message.text

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('MindTech Solutions', 'CodeWave Ltd.', 'TechFusion Labs', 'DataPulse Solutions', 'CloudTech Innovations')

    bot.send_message(chat_id, "Выберите исполнителя:", reply_markup=markup)
    bot.register_next_step_handler(message, process_executor_step, project_name, project_description)


def process_executor_step(message, project_name, project_description):
    # сохраняем выбор исполнителя и завершаем общение
    chat_id = message.chat.id
    executor = message.text
    bot.send_message(chat_id, "Ваша заявка принята. Ждите обратной связи")

def second_menu(message):
    if message.text == "Графики":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Таблица")
        item2 = types.KeyboardButton("Круговая диаграмма")
        item3 = types.KeyboardButton("График рассеяния")
        item4 = types.KeyboardButton("Гистограмма")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Графики":
        second_menu(message)
    if message.text == "Назад":
        chat_id = message.chat.id
        bot.send_message(chat_id, "Спасибо, что вопользовались ботом!")
    if message.text == "Таблица":
        photo = open('Таблица.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Круговая диаграмма":
        photo = open('Круговая диаграмма.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "График рассеяния":
        photo = open('График рассеяния.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Гистограмма":
        photo = open('Гистограмма.png', 'rb')
        bot.send_photo(message.chat.id, photo)


# Запуск бота
bot.polling()