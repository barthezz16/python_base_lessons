# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
import threading

from Utils import sort_and_print, total, time_track


class VolatilityAnalyser(threading.Thread):

    def __init__(self, file_to_read, *args, **kwargs):
        # TODO Ох, ну прям глаза режет такое количество атрибутов
        # TODO Большая же часть используется только в одном методе - почему бы их не превратить в обычные переменные?
        super().__init__(*args, **kwargs)
        self.file_to_read = file_to_read
        self.files_to_open = None
        self.data = {}
        self.price_list = []
        self.value = []
        self.average_price = 0
        self.volatility = 0
        self.secid = 0
        self.tradetime = 0
        self.price = 0
        self.quantity = 0
        self.result = {}
        self.zero_volatility = []
        self.min_volatility = {}
        self.max_volatility = {}

    def run(self,):
        self.file_analytics(self.file_to_read)

    def file_analytics(self, file_to_read):
        with open(os.path.join('trades', file_to_read), 'r') as file:
            # analysers = [VolatilityAnalyser(file_to_read=line) for line in file.readlines()[1:]]
            # for analyser in analysers: # вот так уже все работает, но когда я бытаюсь разбить по потокам
            #     analyser.start()  # чтнение строк, все ломается, line из analysers не видна ниже
            # for analyser in analysers: # где я хочу ее распаковать
            # TODO Разбивать по потокам чтение каждой строки не нужно, тогда на обмен информацией уйдет
            # TODO больше времени, разбиения по файлам достаточно
            # TODO т.е. другими словами надо стараться большие монотонные задания, которые можно выполнять независимо
            #     analyser.join()
            for line in file.readlines()[1:]:
                self.secid, self.tradetime, self.price, self.quantity = line.split(',')
                self.price_list.append((float(self.price)))
                self.data[self.secid] = self.price_list
            self.value = list(self.data.values())
            self.average_price = (min(self.value[0]) + max(self.value[0])) / 2
            self.volatility = ((max(self.value[0]) - min(self.value[0])) / self.average_price) * 100
            self.result[self.secid] = self.volatility
            total.update(self.result)

@time_track
def get_file():
        # TODO Тут бы Queue прикрутить или хотя бы Lock использовать
        analysers = [VolatilityAnalyser(file_to_read=files)for files in os.listdir('trades')]
        for analyser in analysers:
            analyser.start()
        for analyser in analysers:
            analyser.join()

get_file()
sort_and_print()

