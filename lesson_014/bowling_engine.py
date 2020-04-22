def analyzing_result(result):
    global analized_res, total
    analized_res = {}
    total = 0
    frames = 0
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    for k, v in analized_res.items():
        frames += 1
        check_errors(v)
        result_count(v)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    print(f'{result} -> {total}')
    print(total)
    return total



def result_count(v):
    global total
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
    return v


def check_errors(v):
    if '0' in v:
        raise ValueError('Введено неправильное значение')
    elif '/' in v[0]:
        raise ValueError('Spare на первом броске')
    elif 'X' in v[1]:
        raise ValueError('Strike на втором броске')
    if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[0]) >= 10:
        raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')


# try:
#     result = 'X34-/1744XX23--4/'
#     analyzing_result(result=result)
# except Exception as exc:
#     print(f'{result} --> {exc}')
# try:
#     result = '12X34-/1744XX23--4/'
#     analyzing_result(result=result)
# except Exception as exc:
#     print(f'{result} -->  {exc}')
# try:
#     result = '1X4-/1744XX23--4/'
#     analyzing_result(result=result)
# except Exception as exc:
#     print(f'{result} -->  {exc}')
# try:
#     result = '/34-/1744XX23--4/'
#     analyzing_result(result=result)
# except Exception as exc:
#     print(f'{result} -->  {exc}')
try:
    result = '9934-/1744XX23--4/'
    analyzing_result(result=result)
except Exception as exc:
    print(f'{result} -->  {exc}')
# try:
#     result = '0534-/1744XX23--4/'
#     analyzing_result(result=result)
# except Exception as exc:
#     print(f'{result} -->  {exc}')

# TODO Добавлю пример. Пусть есть строка result = 'X34-/1744XX23--4/'
# TODO Напишите функцию(а лучше метод), который примет параметром эту строку, а на выходе выдаст
# TODO {1:(X, -), 2:(3, 4), 3:(-, /), 4:(1, 7), 5:(4, 4), 6:(X, -), 7:(X, -), 8:(2, 3), 9:(-, -), 10:(4, /)}
# TODO Тогда можно будет легко проверить строку на наличие ошибок.
# TODO Примеры фреймов с ошибками: (1, X) - страйк на втором броске
# TODO (/, 2) - / на первом броске
# TODO (5, 5) - сумма очков больше 9 (в этом случае должен быть (5, /)
# TODO (0, 2) - вместо 0 должен быть "-"
# TODO Так же надо проверять количесвто фреймов + наличие других символов в строке.
