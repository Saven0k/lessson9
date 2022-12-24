import emoji
'''
3 Создайте программу для игры в "Крестики-нолики".

Вариант интерфейса:

 0  |  1 | 2
--------------
 3  |  4 | 5
--------------
 6  |  7 | 8

'''

first_pl = input("Choose x or o: ")
if first_pl == 'x':
    first_pl = emoji.emojize(':heavy_multiplication_x:' , language='alias')

else:
    first_pl = emoji.emojize(':o:')
second_pl = input("Choose x or o: ")
if second_pl == 'o':
    second_pl = emoji.emojize(':o:', language='alias')
else:
    second_pl = emoji.emojize(':x:',  language='alias')

def play(first_player , second_player):
    lst = []
    for item in range(0 , 9):
        lst.append(None)

    print(f'  Start      \n{lst[0]} / {lst[1]} / {lst[2]}\n-----------------\n{lst[3]} / {lst[4]} / {lst[5]}\n-----------------\n{lst[6]} / {lst[7] } / {lst[8]}')
    print("                             \n                            ")

    for i in range(len(lst)):
        print("First player turn")
        fl_pl_temp = int(input(" first playre choose place(number): "))
        lst[fl_pl_temp] = first_player
        print(f'{lst[0]} / {lst[1]} / {lst[2]}\n-----------------\n{lst[3]} / {lst[4]} / {lst[5]}\n-----------------\n{lst[6]} / {lst[7]} / {lst[8]}')
        print("                             \n                            ")
        if lst[0] == lst[4] == lst[8] == first_player != None or lst[0] == lst[1] == lst[2] == first_player != None or lst[3] == lst[4] == lst[5] == first_player!= None or lst[6] == lst[7] == lst[8] == first_player!= None or lst[2] == lst[4] == lst[6] == first_player!= None:
            print(emoji.emojize(f'  First player WIN :bangbang:        \n{lst[0]} / {lst[1]} / {lst[2]}\n-----------------\n{lst[3]} / {lst[4]} / {lst[5]}\n-----------------\n{lst[6]} / {lst[7]} / {lst[8]}',language='alias' ))
            break
        else:
            print("Second player turn")
            sl_pl_temp = int(input(" second playre choose place(number): "))
            lst[sl_pl_temp] = second_player
            print(f'{lst[0]} / {lst[1]} / {lst[2]}\n-----------------\n{lst[3]} / {lst[4]} / {lst[5]}\n-----------------\n{lst[6]} / {lst[7]} / {lst[8]}')
            print("                             \n                            ")
            if lst[0] == lst[4] == lst[8] == second_player != None or lst[0] == lst[1] == lst[2] == second_player != None or lst[3] == lst[4] == lst[5] == second_player != None or lst[6] == lst[7] == lst[8] == second_player != None or lst[2] == lst[4] == lst[6] == second_player != None:
                print(emoji.emojize(f'  Second player Win :bangbang:       \n{lst[0]} / {lst[2]} / {lst[3]}\n-----------------\n{lst[3]} / {lst[4]} / {lst[5]}\n-----------------\n{lst[6]} / {lst[7]} / {lst[8]}', language='alias'))
                break


play(first_pl , second_pl)