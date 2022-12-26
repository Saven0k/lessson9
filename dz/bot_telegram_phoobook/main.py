import log
import data_import
import data_recording
import search
import view
import  os
from data_import import impt_1

if os.path.exists('DzPapka/logger.txt'):
    path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), ' logger.txt' )
    os.remove(path)




print('                   Телефонный справочник                      ')



log.wr('start')
phonebook = {}

def work():

    print('1 - добавить новую запись\n2 - вывести справочник на экран\n3 - импортировать\n4 - экспорт\n5 - поиск записи\n6 - удаление записи\n 0 - прекратить работу')

    data = int(input("Введи номер желаемой операции: "))

    while data != 0:
        if data == 1:
            log.wr2(f"Человек выбрал  {data}")

            second_name = input("Введите фамилию: ")
            log.wr2(f"Фамилия {second_name}")

            name = input("Введите имя: ")
            log.wr2(f"Имя {name}")

            phone_number = int(input("Введите номер: "))
            log.wr2(f' Номер - {phone_number}')

            info = input("Введите описание: ")
            log.wr2(f"Описание {info}")

            data_recording.write(second_name, name , phone_number , info , phonebook )
            log.wr2("Была сделана запись")
            print("Запись была сделана")
            print('                      \n                            \n                 ')
            work()


        elif data == 2:
            log.wr2(f"Человек выбрал {data}")
            print(*view.read_write())
            print('                      \n                            \n                 ')
            work()


        elif data == 3:
            log.wr2(f"Человек выбрал {data}")
            data3 = int(input(("Выберте файл из которого хотите  импортировать: \n 1 - gg.txt \n 2 - Text.txt \n 3- number.txt ")))
            if data3 == 1:
                log.wr2(f"Человек выбрал {data3}")
                data_import.impt_1()
            elif data3 == 2:
                log.wr2(f"Человек выбрал {data3}")
                data_import.impt_2()
            elif data3 == 3:
                log.wr2(f"Человек выбрал {data3}")
                data_import.impt_3()
            else:
                log.wr2(f"'eror'")
                print("error")
            print('                      \n                            \n                 ')
            work()

        elif data == 4:
            log.wr2(f"Человек выбрал {data}")

            data2 = int(input(("В каком разерешение вы хотите экспортировать данные\n1 - .txt\n2 - .cvs: ")))
            if data2 == 1:
                log.wr2(f"Человек решил экспотировать в виде {data2}")
                export.export_data_txt(phonebook)
            elif data2 == 2:
                log.wr2(f"Человек решил экспотировать в виде {data}")
                export.export_data_exl(phonebook)
            else:
                log.wr2(f"Не получилсоь 'erorr'")
                print("eror")
            print('                      \n                            \n                 ')
            work()
        else:
            log.wr2("End EROR")
            print('                      \n                            \n                 ')
            print('Eerorr')
            print('                      \n                            \n                 ')
            data = 0
            work()

work()


