# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class SortingFiles:
    def __init__(self, folder, new_folder):
        self.reed_folder_normalized = os.path.normpath(folder)
        self.destination_folder_normalized = os.path.normpath(new_folder)
        self.full_file_path = None
        self.secs = None
        self.file_time = None
        self.dir_name = None
        self.dir_name_year = None
        self.dir_name_month = None

    def scan_for_files(self):
        for dirpath, dirnames, filenames in os.walk(self.reed_folder_normalized):
            for file in filenames:
                self.full_file_path = os.path.join(dirpath, file)
                self.secs = os.path.getmtime(self.full_file_path)
                self.file_time = time.gmtime(self.secs)
                self.dir_name_year = str(self.file_time[0])
                self.dir_name_month = str(self.file_time[1])
                os.makedirs(
                    self.destination_folder_normalized + '\\' + str(self.file_time[0]) + '\\' + str(
                        f'{self.file_time[1]:0>2}'),
                    exist_ok=True)
                # TODO Отлично, только self.destination_folder_normalized + '\\' + str(self.file_time[0]) + '\\' + str(
                #                         f'{self.file_time[1]:0>2}')
                # TODO Вот этот путь отдельно сформируйте при помощи join(чтобы на других ОС можно было с ним работать)
                shutil.copy2(self.full_file_path,
                             self.destination_folder_normalized + '\\' + str(self.file_time[0]) + '\\' + str(
                                 f'{self.file_time[1]:0>2}') + '\\' + file)
                # TODO + тут можно будет заменить этот путь на переменную, дублирования будет меньше

    def run(self):
        self.scan_for_files()


sorter = SortingFiles(folder='icons', new_folder='icons_by_year')
sorter.run()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
