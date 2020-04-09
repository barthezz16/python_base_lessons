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


# 1) создавать в словаре по ключу новую запись (nok_count[str(line[1:-16])] = 1)
# 2) возвращать старое значение (предыдущую минуту) и по этой минуте значение по этому ключу через yield
# 3) заменять старое значение на новое


def stat_collector(file_name):
    nok_counter = 0
    item_to_find = 'NOK'
    with open(file_name, mode='r') as file:
        previous_line = {}
        while True:
            line = file.readline()
            if item_to_find in line:
                if line[1:-16] == previous_line:
                    nok_counter += 1  # TODO у меня была такая же версия, когда я пробовал решить еще сам,
                    # TODO но тогда я не подумал что так просто счетчик можно сделать, искал какието сложные пути,
                    # TODO теперь я понял замечания Вадима в лекциях, что не надо все усложнять....
                else:
                    yield previous_line, nok_counter
                    previous_line = line[1:-16]
                    nok_counter = 1


file_name = 'events.txt'

grouped_events = stat_collector(file_name)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
