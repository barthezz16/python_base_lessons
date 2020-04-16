import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


def sort_and_print(param):
    global item_to_find, list
    sorted_total = list(sorted(total.items(), key=lambda x: x[1], reverse=True))
    dict_total = dict(sorted_total)
    item_to_find = 0.0
    for _ in range(4):
        for i, sub_list in enumerate(sorted_total):
            if item_to_find in sub_list:
                del sorted_total[i]
    for k, v in dict_total.items():
        if v == 0.0:
            zero_volatility.append(k)
    print('Максимальная волатильность:')
    for list in sorted_total[:3]:
        secid, volatility = list
        print(' ' * 4, secid, '-', volatility, '%')
    print('Минимальная волатильность:')
    for list in sorted_total[-3::]:
        secid, volatility = list
        print(' ' * 4, secid, '-', volatility, '%')
    print('Нулевая волатильность:')
    print(' ' * 4, ', '.join(zero_volatility))


total = {}
zero_volatility = []
