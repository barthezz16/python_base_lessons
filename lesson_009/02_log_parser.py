# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class LogParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.item_to_find = 'NOK'

    def stat_collector_by_minutes(self):
        with open(self.file_name, mode='r') as file:
            for line in file:
                if self.item_to_find in line:
                    if str(line[1:-16]) in self.stat:
                        self.stat[str(line[1:-16])] += 1
                        return line
                    else:
                        self.stat[str(line[1:-16])] = 1

    def stat_collector_by_hours(self):
        with open(self.file_name, mode='r') as file:
            for line in file:
                if self.item_to_find in line:
                    if str(line[1:-19]) in self.stat:
                        self.stat[str(line[1:-19])] += 1
                        return line
                    else:
                        self.stat[str(line[1:-19])] = 1

    def print_by_minutes(self, line):
        print(f'[{str(line[1:-16]):^16}]' + f'{self.stat.get(str(line[1:-16])):^5}')

    def print_by_hours(self, line):
        print(f'[{str(line[1:-19]):^12}]' + f'{self.stat.get(str(line[1:-19])):^5}')


parser = LogParser(file_name='events.txt')
minutes_line = parser.stat_collector_by_minutes()
parser.print_by_minutes(line=minutes_line)
hours_line = parser.stat_collector_by_hours()
parser.print_by_hours(line=hours_line)


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
