# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 4 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – strike всегда 20 очков
#   «4/» - spare всегда 15 очков
#   «34» – сумма 3+4=7
#   «-4» - сумма 0+4=4
# То есть для игры «Х4/34-4» сумма очков равна 20+15+7+4=46
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.
import argparse
from random import randint

from termcolor import cprint

PINS = 10
FRAME = 10


# class Bowling:
#
#     def __init__(self):
#         self.pins = 10
#         self.remaining_pins = 0
#         self.score = 0
#
#     def run(self):
#         total_score = []
#         for _ in range(FRAME):
#             cprint('*' * 45, color='green')
#             cprint(f'Фрейм # {_ + 1}', attrs=['bold'], color='yellow')
#             try_result = []
#             self.remaining_pins = PINS
#             throw_bowling_ball_try = 1
#             self.throw_ball(throw_bowling_ball_try, total_score, try_result)
#
#     def throw_ball(self, throw_bowling_ball_try, total_score, try_result):
#         while self.remaining_pins > 0 <= 10 and throw_bowling_ball_try <= 2:
#             throw = randint(0, self.remaining_pins)
#             self.remaining_pins -= throw
#             throw_bowling_ball_try += 1
#             print('Бросок #', throw_bowling_ball_try,
#                   'сбито кеглей', throw if throw > 0 else '-',
#                   'осталось кеглей', self.remaining_pins,
#                   )
#             if throw == 10:
#                 try_result.append(20)
#                 cprint('***!STRIKE!***', color='red')
#             elif self.remaining_pins == 0:
#                 try_result.append(15 - try_result[0])
#                 cprint('SPARE', color='red')
#             else:
#                 try_result.append(throw)
#         self.get_score(total_score, try_result)
#
#     def get_score(self, total_score, try_result):
#         total_score.append(sum(try_result))
#         print('всего очков', sum(total_score))
#
#
# game = Bowling()
# game.run()


def bowling(total_score):  # TODO Параметр выходит не используется внутри функции? Тогда зачем он?
    total_score = []  # TODO Тут он сразу перезаписывается
    for _ in range(FRAME):
        try_result = []
        remaining_pins = PINS
        throw_bowling_ball_try = 1
        while remaining_pins > 0 <= 10 and throw_bowling_ball_try <= 2:
            throw = randint(0, remaining_pins)
            remaining_pins -= throw
            throw_bowling_ball_try += 1
            if throw == 10:
                try_result.append(20)
            elif remaining_pins == 0:
                try_result.append(15 - try_result[0])
            else:
                try_result.append(throw)
        total_score.append(sum(try_result))
    print('всего очков', sum(total_score))

# TODO Я бы советовал первым этапом научиться правильно разделять строку на фрэймы
# TODO Тогда же можно будет проверить, состоит ли строка из 10 фреймов и правильные ли он
# TODO А уже потом считать очки. + нужно вынести основной код в движок, а тут оставить только импорты и аргпарс
parser = argparse.ArgumentParser()
parser.add_argument('result', help='Show game result')
args = parser.parse_args()

bowling(args.result)

# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state
