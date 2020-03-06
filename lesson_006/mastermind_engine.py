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
    _numbers = [randint(0, 9) for n in range(digits_amount)]  # Вопрос, что такое n в этой строке?
    # TODO n это переменная цикла, как
    # for n in range(...)
    #     список.append(randint())
    # TODO Как я и писал раньше - число в итоге может получиться неправильным
    # TODO Нужно использовать другой способ генерирования 4 чисел
    return _numbers


def compare_numbers():
    cows = 0
    bulls = 0
    player_try = input(int())  # TODO Ввод пользователя надо получать параметром и опять же input(int()) не то же
    # TODO что int(input())
    for x in range(0, digits_amount):
        if player_try[x] == _numbers[x]:
            bulls += 1
        elif player_try[x] in _numbers:
            cows += 1
            return cows, bulls  # TODO Возврат идёт не в том месте
        # TODO получается, что после первой найденной "коровы" сработает return
        # TODO а он должен быть после цикла (обратите внимание на отступ, он определяет к чему относиться часть кода)
