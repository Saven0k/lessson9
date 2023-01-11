import log
import time
tm = time.asctime()
def write(scn, nm, ph, inf):
    phonebook = {}
    log.wr2('Создан справочник')
    phonebook[f'{scn}'] = nm, ph, inf, tm
    log.wr2('Добавленны данные в  справочник')
    save_phones(phonebook)


def ww(data):
    save_phones(data)
def save_phones(data):
    with open('phonesbook.txt', 'a') as f:
        f.write(f'{data}\n')
