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
import csv
import json
from datetime import datetime, timedelta
from decimal import Decimal
import re
from termcolor import cprint


class DungeonGame:

    def __init__(self):
        self.re_location = r'\w+_*\w*(\d+)*_tm(\d+).*\d+'
        self.re_mobs = r'\w+_exp(\d+)_tm(\d+)'
        self.current_location_name = 'Location_0_tm0'
        self.re_exit = r'Hatch_tm159.098765432'
        self.location = data_from_file['Location_0_tm0']
        self.mob_list = []
        self.location_list = []
        self.exp = 0
        self.time_elapsed = datetime.strptime('00:00', '%M:%S')
        self.remaining_time = '123456.0987654321'
        self.choice = None
        self._try = 0
        self.fight_exit = False

    def run(self):
        while Decimal(self.remaining_time) > 0:
            if self.current_location_name == 'Hatch_tm159.098765432' and self.exp >= 280:
                cprint('Поздраляю вы победитель!', color='red')
                break
            elif self.current_location_name == 'Hatch_tm159.098765432' and self.exp < 280:
                print('Вы нашли выход, НО у вас недостаточно опяты для открытия двери! ')
                break
            else:
                self._try += 1
                self.mob_list = []
                self.location_list = []
                self.print_and_data_check()
                if self._try == 1:
                    self.mob_list_update()
                self.location_list_update()
                self.player_choice()
                if int(self.choice) == 1:
                    while len(self.mob_list) != 0:
                        self.kill_monster()
                        if self.fight_exit:
                            break
                    self.writer()
                elif int(self.choice) == 2:
                    self.location_change()
                    self.writer()
                elif int(self.choice) == 3:
                    self.exit()
                    self.writer()
                    break
                else:
                    print('Выбрано неправильное действие. \nПопробуйте еще раз!')
                    self._try = 0
        else:
            print('Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!\nУ вас темнеет в глазах... прощай, принцесса...')
        self.writer()

    def print_and_data_check(self):
        cprint('*' * len(f'У вас {self.exp} опыта и осталось {self.remaining_time} секунд до наводнения'), color='red')
        print(f'Вы находитесь в {self.current_location_name}')
        print(f'У вас {self.exp} опыта и осталось {self.remaining_time} секунд до наводнения')
        print(f'Прошло времени: {self.time_elapsed.time()}')
        cprint('Внутри вы видите:', color='red')

    def location_list_update(self):
        for key, data in enumerate(self.location):
            if isinstance(data, dict):
                self.location_list.append((list(data.keys())[0], key))
                print('— Вход в локацию:', self.location_list[-1][0])

    def mob_list_update(self):
        for key, data in enumerate(self.location):
            if isinstance(data, str):
                self.mob_list.append(data)
                print('— Монстра: ', data)

    def player_choice(self):
        cprint('Выберите действие: ', color='red')
        if len(self.mob_list) > 0 and not self.fight_exit:
            self.choice = input('1) Атаковать монстров на локации. '
                                '\n2) Переход в другую локацию. '
                                '\n3) Сдаться и выйти из игры! ')
        elif self.fight_exit:
            self.choice = input('2) Переход в другую локацию. '
                                '\n3) Сдаться и выйти из игры! ')
        else:
            self.choice = input('1) На локации нет монстров! '
                                '\n2) Переход в другую локацию. '
                                '\n3) Сдаться и выйти из игры! ')

    def location_change(self):
        if len(self.location_list) == 0:
            print('Вы зашли в тупик, вы переноситесь на начало.')
            self.exp = 0
            self.time_elapsed = datetime.strptime('00:00', '%M:%S')
            self.remaining_time = '123456.0987654321'
            self.location = data_from_file["Location_0_tm0"]
            self.current_location_name = "Location_0_tm0"
        else:
            for key, location_name in enumerate(self.location_list, start=1):
                print(f'Перейти в локацию {key} {location_name[0]}')
            choice_to_relocate = input('Выберите локацию для перехода. ')
            while int(choice_to_relocate) > len(self.location_list):
                choice_to_relocate = input('Такого пути нет, попробуйте еще раз! ')
            key, index = self.location_list[int(choice_to_relocate) - 1]
            self.current_location_name = key
            self.location = self.location[int(index)][key]
            time_spend = re.search(self.re_location, key)[2]
            self.remaining_time = Decimal(self.remaining_time) - Decimal(int(time_spend))
            self.time_elapsed = self.time_elapsed + timedelta(seconds=int(time_spend))
            print(f'Вы перешли на новую локацию и потратили на это {Decimal(int(time_spend))} секунд!')
            self._try = 0
            self.fight_exit = False

    def kill_monster(self):
        global key
        if int(self.choice) == 1 and len(self.mob_list) > 0:
            if len(self.mob_list) > 0:
                cprint(f'Похвально, вы выбрали бой! \n!!!Ну что-же начнем!!!', color='red')
                for key, monster_name in enumerate(self.mob_list, start=1):
                    print(f'Атаковать монстра: {key} {monster_name}')
                print(f'Выйти из боя: {key + 1}')
        elif int(self.choice) == 1 and len(self.mob_list) == 0:
            print('Локация полностью зачищенна!')
        choice_to_kill = input('Выберите монстра для атаки. ')
        if int(choice_to_kill) == len(self.mob_list) + 1:
            cprint('Вы вышли из боя.', color='red')
            self.fight_exit = True
        else:
            while int(choice_to_kill) > len(self.mob_list) + 1:
                choice_to_kill = input('Нет такого моба, попробуйте еще раз! ')
            self.mob_list.pop(int(choice_to_kill) - 1)
            gain_exp = Decimal(int(re.search(self.re_mobs, str(self.location))[1]))
            self.exp += gain_exp
            time_spend = re.search(self.re_mobs, str(self.location))[2]
            self.remaining_time = Decimal(self.remaining_time) - Decimal(int(time_spend))
            self.time_elapsed = self.time_elapsed + timedelta(seconds=int(time_spend))
            print(f'Поздравляю, вы убили моба и вы получили {gain_exp} опыта и потратили на это '
                  f'{Decimal(int(time_spend))} секунд!')
            print(f'У вас {self.exp} опыта и осталось {self.remaining_time} секунд до наводнения')
            print(f'Прошло времени: {self.time_elapsed.time()}')

    def exit(self):
        print('Вы уходите? \nНичего, в следующий раз получится!')

    def writer(self):
        result = [{'current_location': self.current_location_name,
                   'current_experience': self.exp,
                   'current_date': str(self.time_elapsed.time())
                   }
                  ]

        with open('dungeon.csv', 'a', encoding='utf8') as result_file:
            writer = csv.DictWriter(result_file, fieldnames=['current_location', 'current_experience', 'current_date'])
            writer.writerows(result)


with open('rpg.json', 'r', encoding='utf8') as file_with_data:
    data_from_file = json.load(file_with_data)

with open('dungeon.csv', 'w', encoding='utf8') as result_header:
    writer_header = csv.DictWriter(result_header, fieldnames=['current_location', 'current_experience', 'current_date'])
    writer_header.writeheader()

start_game = DungeonGame()
start_game.run()
