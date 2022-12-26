from telebot import types , TeleBot
import log
import view
import emoji
import data_recording
import os
TOKEN = ''

PHONEBOOK = {}

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'помогите'])
def start(msg):
    log.wr2('start')
    marcup_inline = types.InlineKeyboardMarkup()
    item_new_entry = types.InlineKeyboardButton(text='Добавить новую запись ', callback_data='new_entry')
    item_view = types.InlineKeyboardButton(text='Показать все записи', callback_data='view')
    item_import = types.InlineKeyboardButton(text='Импортировать', callback_data='import')
    item_export = types.InlineKeyboardButton(text='Экспорт', callback_data='export')
    item_search = types.InlineKeyboardButton(text='Поиск записи', callback_data='search')
    marcup_inline.add(item_new_entry,  item_export, item_search, item_import, item_view)
    bot.send_message(chat_id=msg.from_user.id, text=emoji.emojize(
        f'Привет {msg.from_user.username}, это бот в который встроен телефонный справочник\n У меня не много функций, но я удобный:smiling_imp: \n/start - начать\n/help - помощь\n/log-росмотреть логи\n\n\nА теперь я хочу узнать у тебя что  ты хочешь сделать\n(выбири и нажми на кнопочку :point_down:)',
        language='alias'),
                     reply_markup=marcup_inline)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'new_entry':
        log.wr2(f"Пользователь {call.from_user.username} делает новую запись")
        bot.send_message(chat_id=call.from_user.id, text=emoji.emojize('Введите фамилию:wink:, имя:satisfied: , номер телефона:iphone: , информацию:book: ', language='alias'))
        @bot.message_handler()
        def we(msg):
            second_name, name, phone_number, info = map(str, msg.text.split())
            data_recording.write(second_name, name, phone_number, info, PHONEBOOK)
            log.wr2(f"Пользователь {msg.from_user.username} сделал запись {second_name , name , phone_number, info}")
            bot.send_message(chat_id=msg.from_user.id, text=emoji.emojize('Запись сделана:heavy_check_mark:', language='alias'))
            #print(PHONEBOOK)
    elif call.data == 'view':
        bot.send_message(chat_id=call.from_user.id, text=f'{view.read_write()}\n')
        log.wr2(f"Пользователь {call.from_user.username} посмотрел свои записи")

    elif call.data == 'import':
        log.wr2(f'Пользователь {call.from_user.username} решил имортировать')
        @bot.message_handler(content_types=['document'])
        def answer(msg: types.Message):
            filename = msg.document.file_name
            with open(filename, 'wb') as file:
                file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
            bot.send_message(chat_id=msg.from_user.id, text='Вывожу логыыыы')

    elif call.data == 'export':
        log.wr2(f'Пользователь {call.from_user.username} решил экспортировать справочник')
        bot.send_message(chat_id=call.from_user.id, text='Как думаешь я точно отправлю?(да/нет')
        @bot.message_handler()
        def export(msg):
            bot.send_message(chat_id=call.from_user.id, text='ихихиххи я все сделал идеально')
            bot.send_document(msg.chat.id, open('phonesbook.txt', 'rb'))
            log.wr2(f'Пользователь {call.from_user.username} эксортировал файл phonesbook.txt')


    elif call.data == 'search':
        bot.send_message(chat_id=call.from_user.id, text=emoji.emojize('Введите фамилию человека  для поиска', language='alias'))
        @bot.message_handler()
        def seerch(msg):
            log.wr2(f'Пользователь{msg.from_user.username} ищет человка с фамилией {msg.text}')
            #data = view.oppen()
            ##data1 = ' '.join(data)
            #data2 = {
            #}
            #print(f'{data}')
            if msg.text in data1:
                bot.send_message(chat_id=call.from_user.id, text=f'У вас есть  такой контакт : {str(data1[msg.text])}')
                log.wr2(f"Пользователь {msg.from_user.username} нашел свой контакт")
            else:
                log.wr2(f"Пользователь {msg.from_user.username} не нашел свой контакт")
                marcup_inline2 = types.InlineKeyboardMarkup()
                item_new_yes = types.InlineKeyboardButton(text='Да ', callback_data='yes')
                item_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
                marcup_inline2.add(item_new_yes, item_no)
                bot.send_message(chat_id=call.from_user.id, text=f'У вас нет нет такого контакта хотите создать?', reply_markup=marcup_inline2)
                @bot.callback_query_handler(func = lambda call: True)
                def seerch_up(call):
                    if call.datta == 'yes':
                        log.wr2(f"Пользователь {call.from_user.username} создает новый контакт")
                        bot.send_message(chat_id=call.from_user.id, text=emoji.emojize('Введите фамилию:wink:, имя:satisfied: , номер телефона:iphone: , информацию:book: ', language='alias'))
                        @bot.message_handler()
                        def ask(msg):
                            second_name, name, phone_number, info = map(str, msg.text.split())
                            data_recording.write(second_name, name, phone_number, info, PHONEBOOK)
                            log.wr2(f"Пользователь {msg.from_user.username} сделал запись {second_name, name, phone_number, info}")
                            bot.send_message(chat_id=msg.from_user.id,
                                             text=emoji.emojize('Запись сделана:heavy_check_mark:', language='alias'))

                    elif call.datta == 'no':
                        log.wr2(f"Пользователь {call.from_user.username} не создает новый контакт")
                        bot.send_message(chat_id=call.from_user.id, text=emoji.emojize(f'ну и ладно :pensive:', language='alias'))
    else:
        bot.send_message(chat_id=call.from_user.id, text='Error')
        log.wr2("error")




@bot.message_handler(commands=['log'])
def log1(msg):
    with open('logger.txt', 'r') as f:
        data = str(f'{f.read()}\n')
        bot.send_message(chat_id=msg.from_user.id,text=data)





bot.polling()