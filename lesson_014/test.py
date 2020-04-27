from pprint import pprint


def analyzing_result(result):
    global analized_res, total
    analized_res = {}
    total = 0
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
        for k, v in analized_res.items():
            # print(v[0])
            if 'X' in v:
                analized_res[k] = 10
            elif '-' in v[0]:  # TODO Максим, я что то опять туплю, не понимаю как именно мне заменить
                analized_res.update(
                    {v[0]: 0})  # TODO определенный элемент в значении, пример ('-', '/') --> (0, '/') -->
            # elif '-' in v[1]:   # TODO (0, 10)
            #     analized_res[v[1]] = 0
            # elif '/' in v[1]:
            #     analized_res[k][v[1]] = 10 - v[0]
    print(analized_res)


# TODO может быть на совсем верно, но хочу все значения в цифры перевести, мне кажется так лешче будет... TODO {1:
#  10, 2: ('3', '4'), 3: (0, 10), 4: ('1', '7'), 5: ('4', '4'), 6: 10, 7: 10, 8: ('2', '3'), 9: (0, 0), 10: ('4', 6)}
result = 'X34-/1744XX23--4/'
analyzing_result(result)
