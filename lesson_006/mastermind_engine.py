# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint


def make_number(digits_amount=4):
    global _numbers
    _numbers = [randint(0, 9) for n in range(digits_amount)]
    # почему эта переменная создается как кортеж а не список
    print(type(_numbers), _numbers)  # TODO Не понимаю о чём вы, эта переменная является списком


def compare_numbers(player_try):
    if player_try == _numbers:
        print('Вы выиграли')  # TODO Не нужно проверять частный случай победы,
        # TODO Эта функция нужна только для подсчета быков и коров,
        # TODO А уже в главном модуле будет проверка количества быков и выведение результата
    else:
        cows = 0
        bulls = 0
        print(player_try, 'player_try')
        print(_numbers, '_numbers')
        for x in range(0, digits_amount):
            if player_try[x] == _numbers[x]:  # похоже изза этого и не считается количество быклов и коров
                bulls += 1
            elif player_try[x] in _numbers:
                cows += 1
            return cows, bulls  # TODO Не считается потому что происходит return на первой же итерации
        # TODO возвращать результат надо после цикла, а не в нём (следите за отступом)


_numbers = ()
digits_amount = 4
count = 0
