import telebot
from telebot import types, TeleBot


import config

bot: TeleBot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("09.03.01 Информатика и вычислительная техника")
    item2 = types.KeyboardButton("40.03.01 Юриспруденция")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>James</b>, бот созданный чтобы показывать расписание для первокурсников.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '09.03.01 Информатика и вычислительная техника':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Четная неделя", callback_data='chet01')
            item2 = types.InlineKeyboardButton("Нечетная неделя", callback_data='nechet01')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Выбери четность/нечетность недели', reply_markup=markup)

        elif message.text == '40.03.01 Юриспруденция':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Четная неделя", callback_data='chet02')
            item2 = types.InlineKeyboardButton("Нечетная неделя", callback_data='nechet02')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Выбери четность/нечетность недели', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'chet01':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Понедельник", callback_data='monday01chet')
                item2 = types.InlineKeyboardButton("Вторник", callback_data='tuesday01chet')
                item3 = types.InlineKeyboardButton("Среда", callback_data='wednesday01chet')
                item4 = types.InlineKeyboardButton("Четверг", callback_data='thursday01chet')
                item5 = types.InlineKeyboardButton("Пятница", callback_data='friday01chet')

                markup.add(item1, item2, item3, item4, item5)

                bot.send_message(call.message.chat.id, 'Выбери день недели', reply_markup=markup)

            if call.data == 'monday01chet':

                    bot.send_message(call.message.chat.id, '<b>Понедельник(четная неделя):</b> \n\n<b>8:00 - 9:30 '
                                                           '\n\nМатематика(лекция)</b> \nдоцент Кульпина Т.А.,'
                                                           '120б \n\n<b>9:35 - 11:05 \n\nМатематика(пр.зан.)</b> '
                                                           '\nдоцент Кульпина Т.А. 120б \n\n<b>11:00 - 12:40 \n\nЭкономическая '
                                                           'теория(лекция)</b> \nдоцент Семенова Е.И.,120б'
                                     '\n\n<b>13:10 - 14:40 \n\nЭкономическая теория(пр.зан.)</b> \nдоцент Семенова Е.И.,120б',parse_mode='html')

            if call.data == 'tuesday01chet':

                    bot.send_message(call.message.chat.id, '<b>Вторник(четная неделя):</b>'
                                     '\n\n<b>13:10 - 14:40\n\n1 Группа\n\nИностранный язык(лаб.зан.)</b> \nдоцент Яковлева О.В.,217б'
                                     '\n\n<b>2 Группа \n\nФизическая культура и спорт(лаб.зан.)</b> \nдоцент Петрова Т.Н.',parse_mode='html')

            if call.data == 'wednesday01chet':

                        bot.send_message(call.message.chat.id, '544')

            if call.data == 'nechet01':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Понедельник", callback_data='monday01nechet')
                item2 = types.InlineKeyboardButton("Вторник", callback_data='tuesday01nechet')
                item3 = types.InlineKeyboardButton("Среда", callback_data='wednesday01nechet')
                item4 = types.InlineKeyboardButton("Четверг", callback_data='thursday01nechet')
                item5 = types.InlineKeyboardButton("Пятница", callback_data='friday01nechet')

                markup.add(item1, item2, item3, item4, item5)

                bot.send_message(call.message.chat.id, 'Выбери день недели', reply_markup=markup)

            if call.data == 'chet02':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Понедельник", callback_data='monday02chet')
                item2 = types.InlineKeyboardButton("Вторник", callback_data='tuesday02chet')
                item3 = types.InlineKeyboardButton("Среда", callback_data='wednesday02chet')
                item4 = types.InlineKeyboardButton("Четверг", callback_data='thursday02chet')
                item5 = types.InlineKeyboardButton("Пятница", callback_data='friday02chet')

                markup.add(item1, item2, item3, item4, item5)

                bot.send_message(call.message.chat.id, 'Выбери день недели', reply_markup=markup)
            if call.data == 'nechet02':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Понедельник", callback_data='monday02nechet')
                item2 = types.InlineKeyboardButton("Вторник", callback_data='tuesday02nechet')
                item3 = types.InlineKeyboardButton("Среда", callback_data='wednesday02nechet')
                item4 = types.InlineKeyboardButton("Четверг", callback_data='thursday02nechet')
                item5 = types.InlineKeyboardButton("Пятница", callback_data='friday02nechet')

                markup.add(item1, item2, item3, item4, item5)

                bot.send_message(call.message.chat.id, 'Выбери день недели', reply_markup=markup)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
