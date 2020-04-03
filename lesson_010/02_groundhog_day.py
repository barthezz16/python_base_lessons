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


class IamGodError(Exception):

    def __str__(self):
        return f'на {day} день, почувствовал себя богом'


class DrunkError(Exception):

    def __str__(self):
        return f'на {day} день, напился'


class CarCrashError(Exception):

    def __str__(self):
        return f'на {day} день, попал в аварию'


class GluttonyError(Exception):

    def __str__(self):
        return f'на {day} день, нехватка сахара'


class DepressionError(Exception):

    def __str__(self):
        return f'на {day} день, впал в депрессию'


class SuicideError(Exception):
    def __str__(self):
        return f'на {day} день, покончил жизнь самоубийством'


def one_day():
    global day, ENLIGHTENMENT_CARMA_LEVEL, carma
    day += 1
    dice = randint(0, 13)
    if dice == 13:
        raise exception_list[randint(0, 5)]
    else:
        carma += randint(1, 7)
        return carma


ENLIGHTENMENT_CARMA_LEVEL = 777

day = 0
carma = 0
exception_list = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]

while carma <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        one_day()
    except Exception as exc:
        print(f'{exc}')
else:
    print(f'на {day} день, Достиг просветления!!!')
