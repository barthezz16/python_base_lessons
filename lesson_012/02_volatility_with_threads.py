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

    def __init__(self, file_to_read, lock, *args, **kwargs):
        # TODO согласен, сам хотел убрать
        super().__init__(*args, **kwargs)
        self.file_to_read = file_to_read
        self.data = {}
        self.price_list = []
        self.value = []
        self.result = {}
        self.total_lock = lock

    def run(self, ):
        self.file_analytics(self.file_to_read)

    def file_analytics(self, file_to_read):
        with open(os.path.join('trades', file_to_read), 'r') as file:
            # analysers = [VolatilityAnalyser(file_to_read=line) for line in file.readlines()[1:]]
            # for analyser in analysers: # вот так уже все работает, но когда я бытаюсь разбить по потокам
            #     analyser.start()  # чтнение строк, все ломается, line из analysers не видна ниже
            # for analyser in analysers: # где я хочу ее распаковать
            #  Разбивать по потокам чтение каждой строки не нужно, тогда на обмен информацией уйдет
            #  больше времени, разбиения по файлам достаточно
            #  т.е. другими словами надо стараться большие монотонные задания, которые можно выполнять независимо
            #     analyser.join() # TODO тут не совсем понял...
            for line in file.readlines()[1:]:
                secid, tradetime, price, quantity = line.split(',')
                self.price_list.append((float(price)))
                self.data[secid] = self.price_list
            self.value = list(self.data.values())
            average_price = (min(self.value[0]) + max(self.value[0])) / 2
            volatility = ((max(self.value[0]) - min(self.value[0])) / average_price) * 100
            self.result[secid] = volatility
            self.total_lock.acquire()
            total.update(self.result)
            self.total_lock.release()


lock = threading.Lock()


@time_track
def get_file():
    analysers = [VolatilityAnalyser(file_to_read=files, lock=lock) for files in os.listdir('trades')]
    for analyser in analysers:
        analyser.start()
    for analyser in analysers:
        analyser.join()


get_file()
sort_and_print()
