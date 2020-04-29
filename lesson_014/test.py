from bowling_engine import check_errors


def analyzing_result_worldwide(result):
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
        count(k, v)
        print(total)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def count(k, v):
    global total
    if 'X' in v:
        if 'X' in analized_res[k + 1]:
            if 'X' in analized_res[k + 2]:
                total += 30
            elif '-' in analized_res[k + 2][1]:
                total += 20
            else:
                total += 20 + int(analized_res[k + 2][0])
        elif '/' in analized_res[k + 1]:
            total += 20
        elif '-' in analized_res[k + 1][0]:
            total += 10 + int(analized_res[k + 1][1])
        elif '-' in analized_res[k + 1][1]:
            total += 10 + analized_res[k + 1][0]
        else:
            total += 10 + int(analized_res[k + 1][0]) + int(analized_res[k + 1][1])
    if '/' in v:
        if analized_res[k + 1]:
            if 'X' in analized_res[k + 1]:
                total += 20
            elif '-' in analized_res[k + 1][0]:
                total += 10
            else:
                total += 10 + int(analized_res[k + 1][0])
        else:
            total += 10
    if '-' in v:
        total += 0
    else:
        total += int(v[0]) + int(v[1])

# что то вроде вырисовывается, но не могу теперь понять, как сделать проверку на то что есть ли дальше фреймы
# пробовал ставить if analized_res[k + 1] in analized_res, но что то это не сработало
# TODO Можно написать функцию, которая будет получать словарь с номером и возвращать следующий фрэйм.
# TODO В функции, раз уж фрэймы пронумерованы - просто прибавлять +1 к номеру и проверять, если он больше 10
# TODO то возвращать (0, 0), если меньше, то возвращать нужный фрэйм.

result = '12X34-/1744XX23--4/'
analyzing_result_worldwide(result=result)
