
def analyzing_result(result):
    global analized_res, total
    analized_res = {}
    total = 0
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    for k, v in analized_res.items():
        # print(v)
        if 'X' in v:
            total += 20
        elif '/' in v:
            total += 15
        elif '-' in v:
            total += 0
        elif '-' in v:
            total += 0
        else:
            total += int(v[0]) + int(v[1])
    print(total)


result = 'X34-/1744XX23--4/'

analyzing_result(result=result)
# TODO Добавлю пример. Пусть есть строка result = 'X34-/1744XX23--4/'
# TODO Напишите функцию(а лучше метод), который примет параметром эту строку, а на выходе выдаст
# TODO {1:(X, -), 2:(3, 4), 3:(-, /), 4:(1, 7), 5:(4, 4), 6:(X, -), 7:(X, -), 8:(2, 3), 9:(-, -), 10:(4, /)}
# TODO Тогда можно будет легко проверить строку на наличие ошибок.
# TODO Примеры фреймов с ошибками: (1, X) - страйк на втором броске
# TODO (/, 2) - / на первом броске
# TODO (5, 5) - сумма очков больше 9 (в этом случае должен быть (5, /)
# TODO (0, 2) - вместо 0 должен быть "-"
# TODO Так же надо проверять количесвто фреймов + наличие других символов в строке.

result = '12X34-/1744XX23--4/'  # TODO Слишком много фреймов

analyzing_result(result=result)

result = '1X4-/1744XX23--4/'  # TODO страйк на втором броске

analyzing_result(result=result)

result = '/34-/1744XX23--4/'  # TODO '/' на первом месте

analyzing_result(result=result)

result = '9934-/1744XX23--4/'  # TODO 99 - сумма одного фрейма больше 9 очков

analyzing_result(result=result)

result = '0534-/1744XX23--4/'  # TODO 0 должен вызывать ошибку тоже

analyzing_result(result=result)