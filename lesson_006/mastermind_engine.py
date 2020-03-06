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
    _numbers = [randint(0, 9) for n in range(digits_amount)]  #  я понимаю что надо сделать проверку ввода
    return _numbers                                  # но сейчас хочу, чтобы просто заработало, а потом уже проверки вводить.


def compare_numbers(player_try):
    cows = 0
    bulls = 0
    # player_try = input(int())  # TODO Ввод пользователя надо получать параметром и опять же input(int()) не то же
    # TODO что int(input())
    for x in range(0, digits_amount):
        if player_try[x] == _numbers[x]:
            bulls += 1
        elif player_try[x] in _numbers:
            cows += 1
        return cows, bulls
