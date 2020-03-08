# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint


def make_number(digits_amount=4):
    global _numbers  # поидее вот так генерируются неповторяющиеся числа, но почему то
    for i in range(digits_amount + 1):  # в некоторых случаях создается список то из 3 то их 5 чисел...
        # TODO Это происходит потому, что цикл всегда выполняет 5 итераций
        # TODO Но, если попадаются числа, которые уже есть, они не добавляются в список
        # TODO А итерация при этом проходит впустую.
        # TODO Тут скорее подойдет цикл while, с условием "пока чисел не будет 4"
        digit = randint(0, 9)
        if digit not in _numbers:
            _numbers.append(digit)
        if _numbers[0] == 0:
            _numbers[0] == 1  # TODO Это операция сравнения, а не изменения
            # TODO Лучше поступить немного иначе, до цикла добавьте в пустой numbers случайное число от 1 до 9
            # TODO А потом в цикле уже добавляйте числа с проверкой на повторы
    print(_numbers)
    return _numbers


def compare_numbers(player_try):
    cows = 0
    bulls = 0
    for x in range(0, digits_amount):
        if player_try[x] == _numbers[x]:
            bulls += 1
        elif player_try[x] in _numbers:
            cows += 1
    return bulls, cows


_numbers = []
digits_amount = 4
count = 0
