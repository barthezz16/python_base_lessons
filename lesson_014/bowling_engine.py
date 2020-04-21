from random import randint


PINS = 10
FRAME = 10

# TODO Кажется я понял в чём недопонимание. Вы не должно создавать результат игры в функции.
# TODO Вам нужно создать функцию, которая будет полученный результат проверять и считать.
def bowling(*args):
    total_score = []
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


# TODO Добавлю пример. Пусть есть строка result = 'X34-/1744XX23--4/'
# TODO Напишите функцию(а лучше метод), который примет параметром эту строку, а на выходе выдаст
# TODO {1:(X, -), 2:(3, 4), 3:(-, /), 4:(1, 7), 5:(4, 4), 6:(X, -), 7:(X, -), 8:(2, 3), 9:(-, -), 10:(4, /)}
# TODO Тогда можно будет легко проверить строку на наличие ошибок.
# TODO Примеры фреймов с ошибками: (1, X) - страйк на втором броске
# TODO (/, 2) - / на первом броске
# TODO (5, 5) - сумма очков больше 9 (в этом случае должен быть (5, /)
# TODO (0, 2) - вместо 0 должен быть "-"
# TODO Так же надо проверять количесвто фреймов + наличие других символов в строке.