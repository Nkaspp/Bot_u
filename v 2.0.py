import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from db_predmet import list_predmet, list_bio_mag, list_math, list_physics, list_chem
import random
import os


bot = telebot.TeleBot("5817137852:AAGiMvHxhna8a83LxT0C0g6zpbct5g8F51k", parse_mode=None)
back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu")


def except_message(callback_query):
    keyboard = InlineKeyboardMarkup()
    bot.send_photo(callback_query.from_user.id, open('scedl/exception.jpg', 'rb'))
    keyboard.add(back_button)
    bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                          text='К сожалению расписание не загружено',
                     reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    buttons_dict = list_predmet.copy()
    keyboard = InlineKeyboardMarkup()
    button_list = [InlineKeyboardButton(text=x, callback_data= x) for x in buttons_dict]
    keyboard.add(*button_list)
    #bot.send_message('Загружаю список направлений',chat_id=message.chat.id) # не работает надпись
    bot.send_message(chat_id=message.chat.id, text="Выбери направление:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data and call.data == ('MainMenu'))
def MainMenu(callback_query: CallbackQuery):
    buttons_dict = list_predmet.copy()
    keyboard = InlineKeyboardMarkup()
    button_list = [InlineKeyboardButton(text=x, callback_data = x) for x in buttons_dict]
    keyboard.add(*button_list)
    bot.send_message(callback_query.from_user.id, text="Выбери направление:", reply_markup=keyboard)

#список из Математика Биология Физика и т.д.
@bot.callback_query_handler(func=lambda call: call.data and call.data in list_predmet)
def course_lvl(callback_query: CallbackQuery):
    #print(callback_query)
    code = callback_query.data
    global back_button
    print(code, 'Выбор маг или бакалавр')
    if code in list_predmet:
        keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=x, callback_data=code+x) for x in ['Бакалавриат','Магистратура',]] #добписать реакицю на каждую кнопку
        keyboard.add(*button_list, back_button)
        # bot.send_message(callback_query.from_user.id, 'Загружаю доступные направления')
        # bot.send_message(callback_query.from_user.id, text=f"{code}\nВыбери степень:",
        #                          reply_markup=keyboard)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                              text = 'Загружаю доступные направления\nВыбери степень',
                              reply_markup=keyboard)
    # Добавить чтоб клавиатура менялась, а не печаталось новое сообщение

#список из годов поступления
@bot.callback_query_handler(func=lambda call: call.data and (call.data.endswith('Бакалавриат') or call.data.endswith('Магистратура')))
def course_year(callback_query: CallbackQuery):
    #global back_button
    if callback_query.data.endswith('Бакалавриат'):
        code = callback_query.data[:-8]
        print(code,  'Выбор года обучения бак')
        buttons_dict = ['2019', '2020', '2021', '2022']
        keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=x, callback_data=code+x) for x in buttons_dict]
        keyboard.add(*button_list, back_button)
        # bot.send_message(callback_query.from_user.id, 'Загружаю доступные года поступления')
        # bot.send_message(callback_query.from_user.id, text="Бакалавриат\nВыбери год поступления:",
        #                          reply_markup=keyboard)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                              text='Загружаю доступные года поступления\n"Бакалавриат\nВыбери год поступления',
                              reply_markup=keyboard)
    if  callback_query.data.endswith('Магистратура'):
        code = callback_query.data[:-9]
        print(code, 'Выбор года обучения маг')
        buttons_dict = ['2021', '2022']
        keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=x, callback_data=code+x) for x in buttons_dict] #добписать реакицю на каждую кнопку
        keyboard.add(*button_list, back_button)
        # bot.send_message(callback_query.from_user.id, 'Загружаю доступные года поступления')
        # bot.send_message(callback_query.from_user.id, text="Магистратура\nВыбери год поступления:",
        #                          reply_markup=keyboard)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                              text='Загружаю доступные года поступления\n"Магистратура\nВыбери год поступления',
                              reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data and (call.data[:-2].endswith('20')) and 'Биология' in call.data)
def course(callback_query: CallbackQuery):
        code = callback_query.data
        print(code, 'Выбор направдения биологии')
        keyboard = InlineKeyboardMarkup()
        #back_button = InlineKeyboardButton(text="Back", callback_data="MainMenu")
        button_list = [InlineKeyboardButton(text=x, callback_data=code + x) for x in list_bio_mag]
        keyboard.add(*button_list, back_button)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выбери кафедру:",
                         reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data and (call.data[:-2].endswith('20')) and 'Математика' in call.data)
def course(callback_query: CallbackQuery):
        code = callback_query.data
        print(code)
        keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=x, callback_data=code + x) for x in list_math]
        keyboard.add(*button_list, back_button)
        #bot.send_message(callback_query.from_user.id, f'Загружаю информацию {code}')
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f"Выбери кафедру:",
                         reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data and (call.data[:-2].endswith('20')) and 'Физика' in call.data)
def course(callback_query: CallbackQuery):
        code = callback_query.data
        print(code)
        keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=x, callback_data=code + x) for x in list_physics]
        keyboard.add(*button_list, back_button)
        #bot.send_message(callback_query.from_user.id, f'Загружаю информацию {code}')
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f"Выбери кафедру:",
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data and (call.data[:-2].endswith('20')) and 'Химия' in call.data)
def course(callback_query: CallbackQuery):
        code = callback_query.data
        print(code)
        keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=x, callback_data=code + x) for x in list_chem]
        keyboard.add(*button_list, back_button)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text = f"{code}\nВыбери кафедру:",
                         reply_markup=keyboard)

#список направлений Биологии
@bot.callback_query_handler(func=lambda call: call.data and any(map(lambda x: x in call.data, list_bio_mag)))
def course(callback_query: CallbackQuery):
    code = callback_query.data
    print(code, 'Печать финального файла Биология')
    if code[8]=='Б':
        lvl = 'Бакалавриат'

    elif code[8]=='М':
        lvl = 'Магистратура'
    try:
        bot.send_photo(callback_query.from_user.id, open('scedl/' + code +'.jpg', 'rb'))
        keyboard = InlineKeyboardMarkup()
        keyboard.add(back_button)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                              text = f'Расписание готово\nБиология\n{lvl}\n{code[11:15]}\n{code[15:]}', reply_markup=keyboard)
    except FileNotFoundError:
        except_message(callback_query)
#список направлений Математика
@bot.callback_query_handler(func=lambda call: call.data and any(map(lambda x: x in call.data, list_math)))
def course(callback_query: CallbackQuery):
    code = callback_query.data
    print(code)
    if code[10]=='Б':
        lvl = 'Бакалавриат'

    elif code[10]=='М':
        lvl = 'Магистратура'
    try:
        bot.send_photo(callback_query.from_user.id, open('scedl/' + code + '.jpg', 'rb'))
        keyboard = InlineKeyboardMarkup()
        keyboard.add(back_button)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                              text= f'Расписание готово\nМатематика\n{lvl}\n{code[13:17]}\n{code[17:]}',
                         reply_markup=keyboard)
    except FileNotFoundError:
        except_message(callback_query)
#список направлений Физика
@bot.callback_query_handler(func=lambda call: call.data and any(map(lambda x: x in call.data, list_physics)))
def course(callback_query: CallbackQuery):
    code = callback_query.data
    print(code)
    if code[6] == 'Б':
        lvl = 'Бакалавриат'

    elif code[6] == 'М':
        lvl = 'Магистратура'
    try:
        bot.send_photo(callback_query.from_user.id, open('scedl/' + code + '.jpg', 'rb'))
        keyboard = InlineKeyboardMarkup()
        keyboard.add(back_button)
        bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                              text= f'Расписание готово\nФизика\n{lvl}\n{code[9:13]}\n{code[13:]}',
                         reply_markup=keyboard)
    except FileNotFoundError:
        except_message(callback_query)
# список направлений Химия
@bot.callback_query_handler(func=lambda call: call.data and any(map(lambda x: x in call.data, list_chem)))
def course(callback_query: CallbackQuery):
        code = callback_query.data
        print(code)
        if code[5] == 'Б':
            lvl = 'Бакалавриат'

        elif code[5] == 'М':
            lvl = 'Магистратура'
        keyboard = InlineKeyboardMarkup()
        keyboard.add(back_button)
        try:
            bot.send_photo(callback_query.from_user.id, open('scedl/' + code + '.jpg', 'rb'))

            bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                                  text= f'Расписание готово\nХимия\n{lvl}\n{code[8:13]}\n{code[13:]}',
                             reply_markup=keyboard)
        except FileNotFoundError:
            bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,
                                  text= f'Химия\n{lvl}\n{code[8:12]}\n{code[12:]}')
            except_message(callback_query)

bot.polling(none_stop=True, interval=0)


#по переменной code выдавать нужный файл магистратура\бакалавриат
#оформить каллбеки для понятной адресации
#переписать чтоб показывалось сообщение что человек выбрал в итоге
# Доделать клавиатуры