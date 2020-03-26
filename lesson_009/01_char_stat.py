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
            print('+{txt:-^21}+'.format(txt='+'))
            print('|{txt:^10}|'.format(txt='Буква') + '{txt:^10}|'.format(txt='Частота'))
            print('+{txt:-^21}+'.format(txt='+'))
            for key in sorted(self.stat):
                if key.isalpha():
                    print(f'|{key:^10}|' + f'{self.stat.get(key):^10}|')
        print('+{txt:-^21}+'.format(txt='+'))
        print('|{txt:^10}|'.format(txt='Итого') + '{txt:^10}|'.format(txt=sum(self.stat.values())))
        print('+{txt:-^21}+'.format(txt='+'))


counter = Counter(file_name='voyna-i-mir.txt.zip')
counter.collect_stat()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
