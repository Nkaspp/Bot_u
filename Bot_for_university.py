import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from db_predmet import list_predmet
import random
import os


bot = telebot.TeleBot("5817137852:AAGiMvHxhna8a83LxT0C0g6zpbct5g8F51k", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуй!')

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Студент", callback_data="students"))
    markup.add(InlineKeyboardButton("Преподаватель", callback_data="educator"))
    bot.send_message(chat_id=message.chat.id, text="Для начала выбери, в качестве кого ты хочешь зайти:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "students")
def students(callback_query: CallbackQuery):
    #some_data_from_sqlite = [('Биология',), ('Физика',), ('Математика',), ('Магистратура',)]  # список кортежей из БД
    some_data_from_sqlite = list_predmet
    buttons_dict = {i: x[0] for i, x in enumerate(some_data_from_sqlite)}
    print(buttons_dict)
    keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu") #Mainmenu пока нет, осталось от изначального кода
    button_list = [InlineKeyboardButton(text=x, callback_data='course'+x) for x in buttons_dict.values()] #добписать реакицю на каждую кнопку
    keyboard.add(*button_list, back_button)
    bot.send_message(callback_query.from_user.id, 'Загружаю список направлений')
    bot.send_message(callback_query.from_user.id, text="Выбери направление:",
                             reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('course'))
def course(callback_query: CallbackQuery):
    code = callback_query.data[6:]
    if code == 'Биология':
    #if code == 'Биология':
        some_data_from_sqlite = [('Бакалавриат',), ('Магистратура',)]  # список кортежей из БД
        buttons_dict = {i: x[0] for i, x in enumerate(some_data_from_sqlite)}
        keyboard = InlineKeyboardMarkup()
        back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu") #Mainmenu пока нет, осталось от изначального кода
        button_list = [InlineKeyboardButton(text=x, callback_data='biol'+x) for x in buttons_dict.values()] #добписать реакицю на каждую кнопку
        keyboard.add(*button_list, back_button)
        bot.send_message(callback_query.from_user.id, 'Загружаю доступные направления')
        bot.send_message(callback_query.from_user.id, text="Биология\nВыбери степень:",
                                 reply_markup=keyboard)
    # if code == 'Физика':
    #     some_data_from_sqlite = [('Бакалавриат',), ('Магистратура',)]  # список кортежей из БД
    #     buttons_dict = {i: x[0] for i, x in enumerate(some_data_from_sqlite)}
    #     keyboard = InlineKeyboardMarkup()
    #     back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu") #Mainmenu пока нет, осталось от изначального кода
    #     button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in buttons_dict.values()] #добписать реакицю на каждую кнопку
    #     keyboard.add(*button_list, back_button)
    #     bot.send_message(callback_query.from_user.id, 'Загружаю доступные направления')
    #     bot.send_message(callback_query.from_user.id, text="Физика\nВыбери степень:",
    #                              reply_markup=keyboard)
    # if code == 'Математика':
    #     some_data_from_sqlite = [('Бакалавриат',), ('Магистратура',)]  # список кортежей из БД
    #     buttons_dict = {i: x[0] for i, x in enumerate(some_data_from_sqlite)}
    #     keyboard = InlineKeyboardMarkup()
    #     back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu") #Mainmenu пока нет, осталось от изначального кода
    #     button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in buttons_dict.values()] #добписать реакицю на каждую кнопку
    #     keyboard.add(*button_list, back_button)
    #     bot.send_message(callback_query.from_user.id, 'Загружаю доступные направления')
    #     bot.send_message(callback_query.from_user.id, text="Математика\nВыбери степень:",
    #                              reply_markup=keyboard)


    # Добавить чтоб клавиатура менялась, а не печаталось новое сообщение


    # else:
    #     keyboard = InlineKeyboardMarkup()
    #     back_button = InlineKeyboardButton(text="Back",
    #                                        callback_data="MainMenu")  # Mainmenu пока нет, осталось от изначального кода
    #     keyboard.add(back_button)
    #     bot.send_message(callback_query.from_user.id, text="Данное направление не загружено",
    #                      reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('biol'))
def course(callback_query: CallbackQuery):
    code = callback_query.data[4:]
    if code == 'Бакалавриат':
        some_data_from_sqlite = [('2021',), ('2022',)]  # список кортежей из БД
        buttons_dict = {i: x[0] for i, x in enumerate(some_data_from_sqlite)}
        keyboard = InlineKeyboardMarkup()
        back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu") #Mainmenu пока нет, осталось от изначального кода
        button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in buttons_dict.values()] #добписать реакицю на каждую кнопку
        keyboard.add(*button_list, back_button)
        bot.send_message(callback_query.from_user.id, 'Загружаю доступные года поступления')
        bot.send_message(callback_query.from_user.id, text="Биология/Бакалавриат\nВыбери год поступления:",
                                 reply_markup=keyboard)
    if code == 'Магистратура':
        some_data_from_sqlite = [('2022',), ('2023',)]  # список кортежей из БД
        buttons_dict = {i: x[0] for i, x in enumerate(some_data_from_sqlite)}
        keyboard = InlineKeyboardMarkup()
        back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu") #Mainmenu пока нет, осталось от изначального кода
        button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in buttons_dict.values()] #добписать реакицю на каждую кнопку
        keyboard.add(*button_list, back_button)
        bot.send_message(callback_query.from_user.id, 'Загружаю доступные года поступления')
        bot.send_message(callback_query.from_user.id, text="Биология/Магистратура\nВыбери степень:",
                                 reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "educator")
def educators(callback_query:CallbackQuery):
        bot.send_message(callback_query.from_user.id, 'Введите ФИО прподавателя')

bot.polling(none_stop=True, interval=0)