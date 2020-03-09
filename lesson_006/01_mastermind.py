# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastermind_engine import make_number, compare_numbers
from termcolor import cprint


# def check_input(player_try):
#     player_try_check = ''.join(map(str, player_try))
#     while player_try_check.isdigit():
#         pass
#         if player_try_check.isdigit() == False:
#             print('Введено неправильное тип!')
#             break

def check_input():
    global user_input
    user_input = input("Угадайте число из 4 знаков ")  # TODO Максим извините что просто удалил тудушки но у меня вопрос
    # TODO : а зачем сюда переносить все проверки?
    while True:  # TODO они же все проходят внизу, тут же мы только проверяем на ввод цифр? И user_input
        if user_input.isdigit():  # TODO может не стоит в while переносить? это же идет одна попытка на отгадывание,
            return user_input  # TODO если введен неправиьный тип, не надо же это как за попытку считать?
        else:  # TODO надо же просто в этой попытку дать пользователю право ввести еще раз значение?
            cprint('Введен неправильный тип! Попробуйте еще раз!', color='red')
            check_input()


count = 0
result = 0
make_number(4)
player_try = []
while True:
    count += 1
    cprint("Попытка " + str(count), color='yellow')
    user_input = check_input()
    player_try = [int(i) for i in str(user_input)]
    if len(player_try) != 4:
        cprint('Вы ввели неправильное значение!', color='red')
        continue
    result = compare_numbers(player_try)
    if result[0] == 4:
        cprint('Вы выиграли, на это у вас ушло ' + str(count) + ' попыток! Хотите еще партию?', color='magenta')
        break
    else:
        result = compare_numbers(player_try)
        print('Быков -', result[0], 'Коров -', result[1])
