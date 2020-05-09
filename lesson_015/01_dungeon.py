# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import json
import re
from datetime import datetime, timedelta
from decimal import Decimal


class DungeonGame:

    def __init__(self):
        self.re_location = r'Location_(\d)_tm(\d+)'
        self.re_mobs = r'Mob_exp(\d+)_tm(\d+)'
        self.re_exit = r'Hatch_tm159.098765432'
        self.location = data["Location_0_tm0"]
        self.mob_list = []
        self.location_list = []
        self.location = {}
        self.exp = 0
        self.time_elapsed = datetime.strptime('00:00', '%M:%S')
        self.remaining_time = '123456.0987654321'
        self.choice = None

    def run(self):
        self.print_and_data_check()
        self.make_a_choice()

    def print_and_data_check(self):
        print(f'Вы находитесь в', str(list(data.keys())[0]))
        print(f'У вас {self.exp} опыта и осталось {self.remaining_time} секунд до наводнения')
        print(f'Прошло времени: {self.time_elapsed.time()}')
        print('Внутри вы видите:')
        for key, item in enumerate(location, start=1):
            self.mob_list_update(item)
            self.location_list_update(item)
        print('Выберите действие:')
        self.kill_or_move()
        return location

    def kill_or_move(self):
        if len(self.mob_list) != 0:
            for key, monster_name in enumerate(self.mob_list, start=1):
                print(f'1) Атаковать монстра {key} {monster_name}')
        for key, location_name in enumerate(self.location_list, start=1):
            print(f'2) Перейти в локацию {key} {location_name}')
        print('3) Сдаться и выйти из игры!')

    def location_list_update(self, item):
        if isinstance(item, dict):
            for value in item:
                self.location_list.extend(item)
                print('— Вход в локацию: ', value)

    def mob_list_update(self, item):
        if isinstance(item, str):
            self.mob_list.append(item)
            print('— Монстра: ', item)

    def make_a_choice(self):
        self.choice = input()
        if int(self.choice[0]) == 3:
            print('Вы уходите? \nНичего, в следующий раз получится!')
        else:
            while not self.choice[0].isdigit() or not self.choice[1].isdigit() or len(self.choice) > 2:
                self.choice = input('Введено непрвильное значение попоробуйте еще раз! ')
            if int(self.choice[0]) == 1:
                while int(self.choice[1]) > len(self.mob_list):
                    self.choice = input('Нет такого моба, попробуйте еще раз! ')
                self.mob_list.pop(int(self.choice[-1]) - 1)
                self.kill_mob()
                self.kill_or_move()
                self.make_a_choice()
            if int(self.choice[0]) == 2:
                while int(self.choice[1]) > len(self.location_list):
                    self.choice = input('Такого пути нет, попробуйте еще раз! ')
                new_location = int(self.choice[-1])
                self.location = self.location[self.location_list[new_location - 1]]

    def kill_mob(self):
        self.exp += Decimal(int(re.search(self.re_mobs, str(location))[1]))
        time_spend = re.search(self.re_mobs, str(location))[2]
        self.remaining_time = Decimal(self.remaining_time) - Decimal(int(time_spend))
        self.time_elapsed = self.time_elapsed + timedelta(seconds=int(re.search(self.re_mobs, str(location))[2]))
        print(f'Поздравляю, вы убили моба и вы получили {self.exp} опыта и потратили на это '
              f'{Decimal(int(time_spend))} секунд!')


with open('rpg.json', 'r', encoding='utf8') as file_with_data:
    data = json.load(file_with_data)

# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']

location = data["Location_0_tm0"]
start_game = DungeonGame()
start_game.run()

# Учитывая время и опыт, не забывайте о точности вычислений!

