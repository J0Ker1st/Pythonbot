import telebot
from telebot import types
import psycopg2


bot = telebot.TeleBot('2066491281:AAFgK8TEdtk5wdMXc-KMqQkWNH3s_A4IHFY')


conn = psycopg2.connect(database="rasp",
                        user="postgres",
                        password="2258",
                        host="localhost",
                        port="5432")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    return result


@bot.message_handler(commands=['start', 'back'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/teachers')
    btn3 = types.KeyboardButton('/timetables')
    btn4 = types.KeyboardButton('/subjects')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id, 'Для того, чтобы узнать все команды пропишите команду /help '
                                      'или нажмите на кнопку Help', reply_markup=markup)


@bot.message_handler(commands=['help'])
def helper(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/teachers')
    btn2 = types.KeyboardButton('/timetables')
    btn3 = types.KeyboardButton('/subjects')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id, 'У вас есть возможность посмотреть список предметов, '
                                      'имена преподавателей и расписание.\n'
                                      'Для того чтобы посмотреть имена преподавателей пропишите команду '
                                      '/teachers или нажмите соответствующую кнопку.\n'
                                      'Для того чтобы посмотреть расписание пропишите команду '
                                      '/timetable или нажмите соответствующую кнопку.\n'
                                      'Для того чтобы посмотреть список предметов пропишите команду '
                                      '/subjects или нажмите соответствующую кнопку.', reply_markup=markup)


@bot.message_handler(commands=['subjects'])
def sub(message):
    text = "SELECT * FROM subject"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects))


@bot.message_handler(commands=['teachers'])
def teach(message):
    text = "SELECT * FROM teacher"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects))


@bot.message_handler(commands=['timetables'])
def timetable(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/понедельник')
    btn2 = types.KeyboardButton('/вторник')
    btn3 = types.KeyboardButton('/среда')
    btn4 = types.KeyboardButton('/четверг')
    btn5 = types.KeyboardButton('/пятница')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id, 'Выбирите на какой день посмотреть расписание', reply_markup=markup)


@bot.message_handler(commands=['понедельник'])
def mon(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    text = "SELECT * FROM timetable WHERE day = 'Понедельник' "
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects), reply_markup=markup)


@bot.message_handler(commands=['вторник'])
def tue(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    text = "SELECT * FROM timetable WHERE day = 'Вторник'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects), reply_markup=markup)


@bot.message_handler(commands=['среда'])
def wed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    text = "SELECT * FROM timetable WHERE day = 'Среда'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects), reply_markup=markup)


@bot.message_handler(commands=['четверг'])
def thu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    text = "SELECT * FROM timetable WHERE day = 'Четверг'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects), reply_markup=markup)


@bot.message_handler(commands=['пятница'])
def fri(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/back')
    markup.add(btn1)
    text = "SELECT * FROM timetable WHERE day = 'Пятница'"
    subjects = execute_read_query(conn, text)
    bot.send_message(message.chat.id, str(subjects), reply_markup=markup)


# Команда чтобы бот не выключился сразу
bot.infinity_polling()