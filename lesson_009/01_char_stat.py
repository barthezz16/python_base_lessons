# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class Counter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_stat(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line[:-1]:
                    if char in self.stat:
                        self.stat[char] += 1
                    else:
                        self.stat[char] = 1
            self.print_header()
            self.sorting_a_to_z()
            self.print_total()
            self.print_header()
            self.sorting_z_to_a()
            self.print_total()


    def print_header(self):
        print('+{txt:-^21}+'.format(txt='+'))
        print('|{txt:^10}|'.format(txt='Буква') + '{txt:^10}|'.format(txt='Частота'))
        print('+{txt:-^21}+'.format(txt='+'))

    def print_total(self):
        print('+{txt:-^21}+'.format(txt='+'))
        print('|{txt:^10}|'.format(txt='Итого') + '{txt:^10}|'.format(txt=sum(self.stat.values())))
        print('+{txt:-^21}+'.format(txt='+'))

    def sorting_a_to_z(self):
        for key in sorted(self.stat):
            if key.isalpha():
                print(f'|{key:^10}|' + f'{self.stat.get(key):^10}|')

    def sorting_z_to_a(self):
        for key in sorted(self.stat, reverse=True):
            if key.isalpha():
                print(f'|{key:^10}|' + f'{self.stat.get(key):^10}|')

    def sorting_0_to_9(self):
        for key in sorted(self.stat, reverse=True):   #TODO что тут я не совсем понял как отсортировать по значаниям так
            if key.isalpha():   # TODO чтобы тут прошла проверка isalpha
                print(f'|{key:^10}|' + f'{self.stat.get(key):^10}|')




counter = Counter(file_name='voyna-i-mir.txt.zip')
counter.collect_stat()

# TODO + надо добавить остальные сортировки
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
