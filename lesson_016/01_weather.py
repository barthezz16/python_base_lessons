# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
from collections import OrderedDict
from pprint import pprint
from PIL import Image, ImageDraw
from bs4 import BeautifulSoup
import requests
import cv2


class WeatherMaker:
    def __init__(self):
        self.weather_dict = OrderedDict({})
        self.response = requests.get(  # TODO тут стоит создать атрибут с URL (кстати сам Url можно параметром задать)
            # TODO А реквесты уже делать в самом методе
            'https://yandex.ru/pogoda/new-york?utm_campaign=informer&utm_content=main_informer&utm_medium'
            '=web&utm_source=home&utm_term=main_number')
    # TODO А где у вас тут происходит управление датами? Или пока этим не занимались?
    # TODO Хорошо бы добавить возможность по диапазону дат получать информацию.
    def get_weather(self):
        if self.response.status_code == 200:
            html_doc = BeautifulSoup(self.response.text, features='html.parser')
            list_of_values = html_doc.find_all('span', {'class': 'temp__value'})
            list_of_names = html_doc.find_all('div', {'class': 'forecast-briefly__name'})
            list_of_weather = html_doc.find_all('div', {'class': 'forecast-briefly__condition'})
            list_of_date = html_doc.find_all('time', {'class': 'time forecast-briefly__date'})
            for names, values, weather, date in zip(list_of_names, list_of_values, list_of_weather, list_of_date):
                self.weather_dict[str(date.text)] = str(values.text), str(weather.text)
            return self.weather_dict


weather_dict = WeatherMaker()
pprint(weather_dict.get_weather())


class ImageMaker:

    def __init__(self):
        # TODO Лучше тут добавить только строки с путями
        # TODO А инициализировать уже картинку в методе.
        # TODO Чтобы была возможность вызывать метод для рисования каждой из открыток
        # TODO Т.е. будем получать данные, для каждого дня вызывать метод рисующий открытку
        self.background_image_cv = cv2.imread('python_snippets/external_data/probe1.jpg')
        self.weather_dict_to_draw = WeatherMaker()  # TODO Лучше собирать разные классы в одном отдельном
        # TODO "менеджере" классов, который будет управлять данными
        self.data = self.weather_dict_to_draw.get_weather()  # TODO сами данные лушче передавать в метод
        # TODO который рисует по итогу текст.
        self.image_pil = Image.open("python_snippets/external_data/probe.jpg")
        self.pixels = self.image_pil.load()
        self.draw = ImageDraw.Draw(self.image_pil)
        self.width = self.image_pil.size[0]
        self.height = self.image_pil.size[1]

    def run(self):
        self.get_data()
        self.white_to_blue()
        self.draw_card()
        # self.view_image()

    def white_to_blue(self):
        for i in range(self.width, -1):
            for j in range(self.height, -1):
                self.draw.line((i, j), (i, i, i * 2))
        self.image_pil.save('python_snippets/external_data/probe1.jpg')
        # пока тоже не совем понял как лучше градиент сделать
        # TODO В целом циклы верные, надо пройти по всем пикселям и закрасить их
        # TODO только цвет надо передавать какой-нибудь параметром
        # TODO Сами цифры для любого цвета можно найти тут https://colorscheme.ru/color-converter.html
        # TODO И далее после каждого ряда увеличивать числа на +1 (только не больше 255)
        # TODO Например передали красный цвет (255, 0, 0)
        # TODO С каждым рядом +1 прибавляем (255, 1, 1) -- (255, 2, 2) и тд

    def get_data(self):
        pass

    def draw_card(self):
        date = input('Дата: ')
        cv2.putText(self.background_image_cv, 'New York',
                    (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 0, 0), 2)
        cv2.putText(self.background_image_cv, self.data[date][0],
                    (0, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        # не совсем тут понял как мне
        # использовать другой шрифт.
        # TODO Используйте cv2.FONT_HERSHEY_COMPLEX лучше, там русские буквы корректно отображаются
        cv2.putText(self.background_image_cv, self.data[date][1],
                    (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        # TODO Названия стоит вынести в атрибуты
        cv2.imwrite('python_snippets/external_data/probe1.jpg', self.background_image_cv)
        self.background_image_cv = Image.open("python_snippets/external_data/probe1.jpg")
        print(self.data[date][1])
        # TODO А вот этот выбор можно произвести при помощи словаря
        # TODO т.е. добавить в атрибуты словарь, в котором названия будут ключами, а пути к картинке значениями
        if self.data[date][1] == 'Небольшой дождь' or 'Дождь':
            img_to_paste = Image.open('python_snippets/external_data/weather_img/rain.png')
        if self.data[date][1] == 'Облачно с прояснениями' or 'Малооблачно':
            img_to_paste = Image.open('python_snippets/external_data/weather_img/cloud.png')
        if self.data[date][1] == 'Ясно':
            img_to_paste = Image.open('python_snippets/external_data/weather_img/sun.png')
        if self.data[date][1] == 'Снег':
            img_to_paste = Image.open('python_snippets/external_data/weather_img/snow.png')
        # TODO Тогда тут можно будет просто по ключу получать путь
        self.background_image_cv.paste(img_to_paste, (400, 25))
        self.background_image_cv.save('python_snippets/external_data/probe1.jpg', 'JPEG')

    def view_image(self):
        cv2.namedWindow('Picture', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Picture', self.background_image_cv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# про базу данных все помню, завтра этим займусь, этот процесс скидываю скорее чтобы проверить, правльно ли
# я двигаюсь
image = ImageMaker()
image.run()
