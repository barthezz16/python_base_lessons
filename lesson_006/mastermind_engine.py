# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import random, randint

_numbers = ()
digits_amount = 4


def make_number(digits_amount=4):
    global _numbers
    _numbers = [randint(0, 9) for n in range(digits_amount)]
    # TODO Это просто и изящно, но не защищает от дублей. Да и 0 может на первое место попасть.
    # TODO Попробуйте усложнить, добавить пару условий, или какой-то другой метод использовать.
    return _numbers


def compare_numbers():
    cows = 0
    bulls = 0
    player_try = input(int())
    for x in range(0, digits_amount):
        if player_try[x] == _numbers[x]:
            bulls += 1
            print('Быков найдено', bulls)  # TODO Печатать тут ничего не нужно
        elif player_try[x] in _numbers:
            cows += 1
            print('Коров найдено', cows)  # TODO Как и здесь
    # TODO Просто после цикла надо будет вернуть return-ом количество быков и коров
    # TODO А уже в том модуле обрабатывать эти числа, при желании выводить их в принте
