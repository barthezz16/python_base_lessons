# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

import argparse
from file_handler import file_handler

# file_to_read = 'tournament.txt'
# file_to_write = 'tournament_result.txt'
#
# file_reader(read_file=file_to_read, write_file=file_to_write)

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', required=True, help='File to read')
parser.add_argument('-o', '--output', required=True, help='File to write', default='tournament_result.txt')
parser.add_argument('-r', '--rules', help='Result count rules l --> local, w --> worldwide', default='local')
args = parser.parse_args()

file_handler(args.input, args.output, args.rules)

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+
#зачет!