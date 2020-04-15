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
import multiprocessing
import os

from Utils import sort_and_print, total, time_track


class VolatilityAnalyser(multiprocessing.Process):

    def __init__(self, file_to_read, collector=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_to_read = file_to_read
        self.data = {}
        self.price_list = []
        self.value = []
        self.result = {}
        self.collector = collector
        self.total = total

    def run(self):
        self.file_analytics(self.file_to_read)

    def file_analytics(self, file_to_read):
        with open(os.path.join('trades', file_to_read), 'r') as file:
            for line in file.readlines()[1:]:
                secid, tradetime, price, quantity = line.split(',')
                self.price_list.append((float(price)))
                self.data[secid] = self.price_list
            self.value = list(self.data.values())
            average_price = (min(self.value[0]) + max(self.value[0])) / 2
            volatility = ((max(self.value[0]) - min(self.value[0])) / average_price) * 100
            self.result[secid] = volatility
            self.total.update(self.result)
            self.collector.put(dict(self.total))


if __name__ == '__main__':
    @time_track
    def get_file():
        collector = multiprocessing.Queue()
        analysers = [VolatilityAnalyser(file_to_read=files, collector=collector) for files in os.listdir('trades')]
        for analyser in analysers:
            analyser.start()
        for analyser in analysers:
            analyser.join()
        while not collector.empty():
            print(collector.get())  # TODO Максим, вот тут и заминка, коллектор то получил все данные,
            # TODO но вот как теперь это передать в Utils в sort_and_print не изменяя их, я что то придумать не могу...


    get_file()
    sort_and_print()

# Зачет!
