# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# TODO Надо не заменять этот код, а превратить его в генератор
# TODO Генератор должен за одно обращение читать данные за одну минуту
# TODO И если начинается следующая минута - возвращать результат за предыдущую
# TODO Для этого надо будет придумать,
# TODO как сохранять текущее время, чтобы сравнивать его с новым временем следующей строки
# TODO И если такая проверка не проходит - то
# 1) создавать в словаре по ключу новую запись (nok_count[str(line[1:-16])] = 1)
# 2) возвращать старое значение (предыдущую минуту) и по этой минуте значение по этому ключу через yield
# 3) заменять старое значение на новое


def stat_collector(file_name):
    nok_count = {}
    item_to_find = 'NOK'
    with open(file_name, mode='r') as file:
        previous_line = 0  # TODO Нужна ещё одна переменная, в которой будет храниться "предыдущая" строчка
        # TODO При нахождении новой строчки - в эту переменную будет записана текущая
        # TODO Можете попробовать отдельно это реализовать
        while True:
            line = file.readline()
            if item_to_find in line:
                if str(line[1:-16]) in nok_count:
                    nok_count[str(line[1:-16])] += 1  # TODO Перед прибавлением нужно создать ключ
                else:
                    nok_count[str(line[1:-16])] = 1
                    yield nok_count



# def stat_collector():
#     with open(file_name, mode='r') as file:
#         for line in file:
#             if item_to_find in line:
#                 if str(line[1:-16]) in nok_count:
#                     nok_count[str(line[1:-16])] += 1
#                 else:
#                     nok_count[str(line[1:-16])] = 1
#         return nok_count


file_name = 'events.txt'


# line = stat_collector()
# for i in nok_count:
#     print(i, nok_count[i])


grouped_events = stat_collector(file_name)
print(grouped_events)
for group_time in grouped_events:
    print(f'[{group_time}]')

# grouped_events = stat_collector(file_name)
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
