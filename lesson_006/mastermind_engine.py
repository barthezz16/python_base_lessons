# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint


# def make_number(digits_amount=4):
#     global _numbers
#     _numbers = [randint(0, 9) for n in range(digits_amount)]
#     print(_numbers)

def make_number(digits_amount=4):
    global _numbers
    _numbers = [randint(0, 9) for n in range(digits_amount)]
    # TODO Теперь нужно и с этой функцией разобраться, чтобы числа загадывались согласно условиям
    print(_numbers)


def compare_numbers(player_try):
    cows = 0
    bulls = 0
    for x in range(0, digits_amount):
        if player_try[x] == _numbers[x]:
            bulls += 1
        elif player_try[x] in _numbers:
            cows += 1
    print('Быков -', bulls, 'Коров -', cows)
    # TODO ПО условию задания
    # Все общение с пользователем делать в текущем модуле.
    # TODO это делается для приближения структуры программы к реальности.
    # TODO Так здесь у нас "движок" с общими функциями, своеобразный бэкэнд, а в том модуле, куда импорт происходит
    # TODO Что-то наподобие фронт-енда, где мы взаимодействуем с пользователем напрямую
    # TODO Создаем удобный интерфейс, красивые разноцветные надписи и выведение результата.
    return bulls


_numbers = ()
digits_amount = 4
count = 0
