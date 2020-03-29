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
        self.line = None

    def stat_collector(self, param):
        with open(self.file_name, mode='r') as file:
            for line in file:
                if self.item_to_find in line:
                    if str(line[1:-param]) in self.stat:
                        self.stat[str(line[1:-param])] += 1
                    else:
                        self.stat[str(line[1:-param])] = 1
            self.print_stat()

    def print_stat(self):
        for i in self.stat:
            print(i, self.stat[i])


param_for_minutes = 16
param_for_hours = 19
param_for_mounth = 25
param_for_year = 28

parser = LogParser(file_name='events.txt')
# TODO Нет, вы не совсем верно меня поняли
# TODO Нужны отдельные методы, которые будут запускать этот коллектор с нужными параметрами
# TODO Представьте, что у вас будет пользователь, который импортирует ваш класс в свой модуль
# TODO И будет пытаться запускать методы. Но без переменных, которые вы указали вне класса - у него ничего не получится
# TODO Для решения этой задачки можно создать 4 метода, которые будут запускать работу с нужными параметрами
parser.stat_collector(param_for_minutes)
parser.stat_collector(param_for_hours)
parser.stat_collector(param_for_mounth)
parser.stat_collector(param_for_year)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
