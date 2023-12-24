import telebot
from telebot import types

API_TOKEN = '6314524501:AAHQ9rsWLZH61oTdv0C8L5kbbPwpSsoWdEA'

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
    bot.send_message(chat_id, "Ваша заявка принята.")


# Запуск бота
bot.polling()
