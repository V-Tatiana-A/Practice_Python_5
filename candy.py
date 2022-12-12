# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

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

candies=150
print(f'Сейчас имеется всего {candies} конфет')
max_take=28
print(f'Брать можно от 1 до {max_take} конфет')
print('Побеждает тот, кто взял последние конфеты. Удачи!')


def player_turn():
    take = int(input('Введите число конфет, которые возьмете: '))
    if 0<take<max_take+1:
        return take
    else:
        print(f'Вы не можете брать больше {max_take} конфет или не брать их вовсе. Попробуйте ещё раз.')
        return player_turn()


def game (candies, turn):
    while candies!=0:
        if turn == 0:
            с_take=candies % (max_take + 1)
            if с_take==0:
                с_take=rnd(0,max_take)
            print(f'Компьютер взял {с_take} конфет')
            candies = candies - с_take
            print(f'Осталось {candies} конфет')
            turn = 1
        elif turn ==1:
            candies=candies-player_turn()
            print(f'Осталось {candies} конфет')
            turn = 0
    else:
        if turn ==1:
            print('Вы проиграли.')
        else:
            print('Вы выиграли!')

game(candies, turn)


