from telebot import TeleBot, types
import Log


TOKEN = ''
bot = TeleBot(TOKEN)\




@bot.message_handler(commands=['start'])
def start(msg):
    Log.wr2("start")
    bot.send_message(chat_id=msg.from_user.id, text=f'/start - начать, узнать команды\nВведите знак операции')

@bot.message_handler()
def Calculator(msg):
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






bot.polling()















