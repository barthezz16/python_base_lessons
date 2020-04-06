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


def stat_collector():
    with open(file_name, mode='r') as file:
        for line in file:
            if item_to_find in line:
                if str(line[1:-16]) in nok_count:
                    nok_count[str(line[1:-16])] += 1
                else:
                    nok_count[str(line[1:-16])] = 1
        return nok_count


file_name = 'events.txt'
nok_count = {}
item_to_find = 'NOK'

line = stat_collector()
for i in nok_count:
    print(i, nok_count[i])


# TODO тут тоже не могу понять, этот итератор/генератор должен заменить всеь код сверху?

# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
