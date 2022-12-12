
from random import randint as rnd
def toss_a_coin():
    print('Вы будете бросать монетку. Выберите сторону - введите орел или решка:')
    imp = input()
    coin1 = ['орел', 'Орел', 'орёл', 'Орёл', 'ОРЕЛ', 'ОРЁЛ']
    coin2 = ['решка', 'Решка', 'РЕШКА']

    if imp in coin1:
        p=1
        с=0
    elif imp in coin2:
        p=0
        с=1
    else:
        print('Введите сторону корреткно')
        exit()
    toss=rnd(0,1)
    if toss==p:
        print('Вы выиграли и ходите первым')
        result=1
    else:
        print('Вы проиграли, компьютер ходит первым')
        result = 0
    return result

turn=toss_a_coin()

if turn==1:
    p_sign='X'
    c_sign='0'
else:
    p_sign = '0'
    c_sign = 'X'


cells = \
        [
            ['—', '—', '—', '—', '—', '—', '—'],
            ['|', 1, '|', 2, '|', 3, '|'],
            ['—', '—', '—', '—', '—', '—', '—'],
            ['|', 4, '|', 5, '|', 6, '|'],
            ['—', '—', '—', '—', '—', '—', '—'],
            ['|', 7, '|', 8, '|', 9, '|'],
            ['—', '—', '—', '—', '—', '—', '—']
        ]

rows = [[cells[1][1], cells[1][3], cells[1][5]],
        [cells[3][1], cells[3][3], cells[3][5]],
        [cells[5][1], cells[5][3], cells[5][5]],
        [cells[1][1], cells[3][1], cells[5][1]],
        [cells[1][3], cells[3][3], cells[5][3]],
        [cells[1][5], cells[3][5], cells[5][5]],
        [cells[1][1], cells[3][3], cells[5][5]],
        [cells[1][5], cells[3][3], cells[5][1]]]

def reinit(cells):
    rows=[[cells[1][1], cells[1][3], cells[1][5]],
    [cells[3][1], cells[3][3], cells[3][5]],
    [cells[5][1], cells[5][3], cells[5][5]],
    [cells[1][1], cells[3][1], cells[5][1]],
    [cells[1][3], cells[3][3], cells[5][3]],
    [cells[1][5], cells[3][5], cells[5][5]],
    [cells[1][1], cells[3][3], cells[5][5]],
    [cells[1][5], cells[3][3], cells[5][1]]]
    return rows


def print_matrix(cells):
    for i in cells:
        for j in i:
            if j=='X':
                print("\033[30m\033[44m{}\033[0m".format(j), end=' ')
            elif j=='0':
                print("\033[30m\033[42m{}\033[0m".format(j), end=' ')
            else:
                print(j, end=' ')
        print()

print_matrix(cells)
move=0

def check(rows):
    for el in rows:
        if el[0]==el[1]==el[2]:
            res=True
            break
        else:
            res = False
    if move==9:
        res=True
    return res

while check(rows)==False:
    if turn == 0:
        if cells[3][3] == 5:
            cells[3][3] = c_sign
            move+=1
            print_matrix(cells)
            turn = 1
        else:
            for row in rows:
                if (row.count('X') == 2 and row.count('0') == 0) or (row.count('0') == 2 and row.count('X') == 0):
                    for el in row:
                        if ((el != 'X') and (el != '0')):
                            for i in range(1,len(cells),2):
                                if el in cells[i]:
                                    ind2 = cells[i].index(el)
                                    cells[i][ind2]=c_sign
                                    move += 1
                                    turn=1
                                    print_matrix(cells)
                                    rows = reinit(cells)
                                    break
                if turn == 1:
                    break
            else:
                if cells[1][1]==1:
                    cells[1][1] = c_sign
                    move += 1
                    turn = 1
                    rows = reinit(cells)
                    print_matrix(cells)
                elif cells[1][5]==3:
                    cells[1][5] = c_sign
                    move += 1
                    turn = 1
                    rows = reinit(cells)
                    print_matrix(cells)
                elif cells[5][1]==7:
                    cells[5][1] = c_sign
                    move += 1
                    turn = 1
                    rows = reinit(cells)
                    print_matrix(cells)
                # elif cells[5][5]==9:
                #     cells[5][5] = c_sign
                #     move += 1
                #     turn = 1
                #     rows = reinit(cells)
                #     print_matrix(cells)
                else:
                    for i in range(1,len(cells),2):
                        for j in range(1,len(cells[i]),2):
                            if ((cells[i][j]!= 'X') and (cells[i][j]!= '0')):
                                cells[i][j]=c_sign
                                move += 1
                                turn = 1
                                rows = reinit(cells)
                                print_matrix(cells)
                                break
                        if turn == 1:
                            break

    else:
        print(f'Введите куда поставить {p_sign}')
        put = int(input())
        for k in range(1,len(cells),2):
            if put in cells[k]:
                ind = cells[k].index(put)
                cells[k][ind] = p_sign
                move += 1
                turn = 0
                rows = reinit(cells)
                print_matrix(cells)
                break
        else:
            print(f'Вы не можете поставить {p_sign} сюда')
else:
    for el in rows:
        if el[0]==el[1]==el[2]:
            if el[0]=='X':
                if p_sign=='X':
                    print('Игра окончена. Вы победили.')
                    break
                else:
                    print('Игра окончена. Вы проиграли.')
                    break
            elif el[0]=='0':
                if p_sign=='0':
                    print('Игра окончена. Вы победили.')
                    break
                else:
                    print('Игра окончена. Вы проиграли.')
                    break
    else:
        print('Игра окончена. Ничья.')







