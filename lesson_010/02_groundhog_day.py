# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777

day = 0
carma = 0


def one_day():  # TODO Вы немного перепутали структуру. Функция должна возвращать карму (от 1 до 7)
    # TODO А уже саму функцию надо обернуть в цикл
    global day, ENLIGHTENMENT_CARMA_LEVEL, carma
    while carma <= ENLIGHTENMENT_CARMA_LEVEL:
        day += 1
        carma += randint(1, 7)  # TODO И нужно либо добавлять карму, либо вызывать ошибку
        # TODO Например выкинуть случайное число, если оно равно 13 - то кидать случайное исключение
        # TODO Иначе добавлять карму.
        # TODO Про случайное исключение - тут тоже стоит взять случайное число
        # TODO и использовать его как индекс для списка в котором можно хранить исключения
        print(day)
        dice = randint(1, 78)
        # print(dice)
        if dice == 13:
            raise IamGodError(message=f'на {day} день, почувствовал себя богом')
        elif dice == 26:
            raise DrunkError(message=f'на {day} день, напился')
        elif dice == 39:
            raise CarCrashError(message=f'на {day} день, попал в аварию')
        elif dice == 52:
            raise GluttonyError(message=f'на {day} день, нехватка сахара')
        elif dice == 65:
            raise DepressionError(message=f'на {day} день, впал в депрессию')
        elif dice == 78:
            raise SuicideError(message=f'на {day} день, покончил жизнь самоубийством')
    else:
        print('Достиг просветления!!!')


class IamGodError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DrunkError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class CarCrashError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class GluttonyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DepressionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class SuicideError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


one_day()
