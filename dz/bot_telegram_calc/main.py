from telebot import TeleBot, types
import Log


TOKEN = ''
bot = TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def start(msg):
    Log.wr2("start")
    marcup_inline = types.InlineKeyboardMarkup()
    item_complex = types.InlineKeyboardButton(text='Комплексные числа ', callback_data='complex')
    item_racion = types.InlineKeyboardButton(text='Рациональные числа', callback_data='racion')
    marcup_inline.add(item_racion, item_complex)
    bot.send_message(chat_id=msg.from_user.id, text=f'/log - логги /start - начать\nВведите знак операции и выберете с какими числами будет проведенна операция  (для изменения чисел запустите заново-/start', reply_markup =  marcup_inline )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'complex':
        @bot.message_handler()
        def Calculator_complex(msg):
            if msg.text == '+':
                Log.wr2(f"Calc work  = +")
                bot.register_next_step_handler(msg, answer_sum_complex)
                bot.send_message(chat_id=msg.from_user.id, text="Введите слагаемые")

            elif msg.text == '-':
                Log.wr2(f"Calc work = -")
                bot.register_next_step_handler(msg, answer_difference_complex)
                bot.send_message(chat_id=msg.from_user.id, text="Введите уменьшаемое и слагаемое")

            elif msg.text == '*':
                Log.wr2(f"Calc work = *")
                bot.register_next_step_handler(msg, answer_multiplication_complex)
                bot.send_message(chat_id=msg.from_user.id, text="Введите множители")

            elif msg.text == '/':
                Log.wr2(f"Calc work = /")
                bot.register_next_step_handler(msg, answer_division_complex)
                bot.send_message(chat_id=msg.from_user.id, text="Введите делимое  и делитель ")

            elif msg.text == '**':
                bot.register_next_step_handler(msg, answer_squaring_complex)
                Log.wr2(f"Calc work = **")
                bot.send_message(chat_id=msg.from_user.id, text="Введите число и нужный индекс степени")

        def answer_sum_complex(msg):
            a, b = map(complex, msg.text.split())
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
            bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_difference_complex(msg):
            a, b = map(complex, msg.text.split())
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a - b}')
            bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_multiplication_complex(msg):
            a, b = map(complex, msg.text.split())
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a * b}')
            bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_division_complex(msg):
            a, b = map(complex, msg.text.split())
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a / b}')
            bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_squaring_complex(msg):
            a, b = map(complex, msg.text.split())
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a ** b}')
            bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

    elif call.data == 'racion':
        @bot.message_handler()
        def Calculator_racion(msg):
            if msg.text == '+':
                Log.wr2(f"Calc work  = +")
                bot.register_next_step_handler(msg, answer_sum)
                bot.send_message(chat_id=msg.from_user.id, text="Введите слагаемые")

            elif msg.text == '-':
                Log.wr2(f"Calc work = -")
                bot.register_next_step_handler(msg, answer_difference)
                bot.send_message(chat_id=msg.from_user.id, text="Введите уменьшаемое и слагаемое")

            elif msg.text == '*':
                Log.wr2(f"Calc work = *")
                bot.register_next_step_handler(msg, answer_multiplication)
                bot.send_message(chat_id=msg.from_user.id, text="Введите множители")

            elif msg.text == '/':
                Log.wr2(f"Calc work = /")
                bot.register_next_step_handler(msg, answer_division)
                bot.send_message(chat_id=msg.from_user.id, text="Введите делимое  и делитель ")

            elif msg.text == '**':
                bot.register_next_step_handler(msg, answer_squaring)
                Log.wr2(f"Calc work = **")
                bot.send_message(chat_id=msg.from_user.id, text="Введите число и нужный индекс степени")


        def answer_sum(msg):
                a , b = map(int, msg.text.split())
                bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
                bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_difference(msg):
                a , b = map(int,  msg.text.split())
                bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a - b}')
                bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_multiplication(msg):
                a , b = map(int, msg.text.split())
                bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a * b}')
                bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_division(msg):
                a , b = map(int , msg.text.split())
                bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a / b}')
                bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')

        def answer_squaring(msg):
                a , b = map(int, msg.text.split())
                bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычетания  {a ** b}')
                bot.send_message(chat_id=msg.from_user.id, text='Введите знак операции ')




@bot.message_handler(commands=['log'])
def log(msg):
    with open('logger.txt', 'r') as f:
        data = str(f'{f.read()}\n')
        bot.send_message(chat_id=msg.from_user.id,text=data)




bot.polling()















