# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint


def make_number(digits_amount=4):
    global _numbers
    _numbers = [randint(0, 9) for n in range(digits_amount)] # TODO почему эта переменная создается как кортеж а не список
    print(_numbers)


def compare_numbers(player_try):
    if player_try == _numbers:
        print('Вы выиграли')
    else:
        cows = 0
        bulls = 0
        for x in range(0, digits_amount):
            if player_try[x] == _numbers[x]: # TODO похоже изза этого и не считается количество быклов и коров
                bulls += 1
            elif player_try[x] in _numbers:
                cows += 1
            return cows, bulls
        print(player_try, 'player_try')
        print(_numbers, '_numbers')


_numbers = ()
digits_amount = 4
count = 0
