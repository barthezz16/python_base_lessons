def rules(result, rules):
    if rules == 'worldwide' or rules == 'w' or rules == 'W':
        analyzing_result_worldwide(result)
    if rules == 'local' or rules == 'l' or rules == 'L':
        analyzing_result(result)


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
    # print(total)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def analyzing_result_worldwide(result):
    global analized_res, total
    analized_res = {}
    total = 0
    frames = -2
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
            analized_res[i + 1] = ('-', '-')
            analized_res[i + 2] = ('-', '-')
    for k, v in analized_res.items():
        frames += 1
        check_errors(v)
        count_worldwide(k, v)
        # print(total)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def count_worldwide(k, v):
    global total
    if 'X' in v:
        if 'X' in analized_res[k + 1]:
            if 'X' in analized_res[k + 2]:
                total += 30
            elif '-' in analized_res[k + 2][0]:
                total += 20
            else:
                total += 20 + int(analized_res[k + 2][0])
        elif '/' in analized_res[k + 1]:
            total += 20
        elif '-' in analized_res[k + 1][0]:
            if '-' in analized_res[k + 1][1]:
                total += 10
            else:
                total += 10 + int(analized_res[k + 1][1])
        elif '-' in analized_res[k + 1][1]:
            total += 10 + int(analized_res[k + 1][0])
        else:
            total += 10 + int(analized_res[k + 1][0]) + int(analized_res[k + 1][1])
    elif '/' in v:
        if 'X' in analized_res[k + 1]:
            total += 20
        elif '/' in analized_res[k + 1][0]:
            raise ValueError('Spare на первом броске')
        elif '-' in analized_res[k + 1][0]:
            total += 10
        else:
            total += 10 + int(analized_res[k + 1][0])
    elif '-' in v[0]:
        if '-' in v[1]:
            total += 0
        elif '/' in v[1]:
            pass
        else:
            total += int(v[1])
    elif '-' in v[1]:
        if '-' in v[0]:
            total += 0
        elif 'X' in v[0]:
            pass
        else:
            total += int(v[0])
    else:
        if v[0].isdigit and v[1].isdigit:
            total += int(v[0]) + int(v[1])


def result_count(v):
    global total
    if 'X' in v:
        total += 20
    elif '/' in v:
        total += 15
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
    if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[1]) >= 10:
        raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')


# result = '12X34-/1744X23454/'  # 3 20 27 38 46 54 69 74 83 93
# # rules(result=result, rules='worldwide')
# result = '3532X332/3/62--62X'  # 8 13 29 35 48 64 72 72 80 90
# rules(result=result, rules='worldwide')

# result = 'XXXXXXXXXX'
# rules(result=result, rules='worldwide')
# result = '0434-/1744XX23--4/'
# rules(result=result, rules='local')
