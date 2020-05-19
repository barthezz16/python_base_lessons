# -*- coding: utf-8 -*-

import copy
import datetime
from decimal import Decimal
import json
import re
import csv
import text

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


class DungeonObject:
    """Игровой объект"""
    def __init__(self, dungeon_object):
        self.name = dungeon_object[0]
        self.time = Decimal(dungeon_object[1])

    def __str__(self):
        return self.name


class Monster(DungeonObject):
    """Монстр"""
    MOB = r'(?:(?:Boss\d{0,3})|(?:Mob))_exp(\d{1,3})_tm(\d+\.?\d*)'

    def __init__(self, dungeon_object):
        super().__init__(dungeon_object)
        self.time = Decimal(dungeon_object[2])
        self.experience = int(dungeon_object[1])


class Location(DungeonObject):
    """Локация"""
    LOCATION = r'Location_[B\d]{1,2}_tm(\d+\.?\d*)'


class Hatch(DungeonObject):
    """Люк"""
    HATCH = r'Hatch_tm(\d+\.?\d*)'


class Hero:
    """Герой"""
    TIME = None
    flag = True

    def __init__(self, name, dungeon_file):
        self.name = name
        self.dungeon = self._load_dungeon(dungeon_file=dungeon_file)
        self.current_session = copy.deepcopy(self.dungeon)
        self.location = None
        self.time = Decimal(remaining_time)
        Hero.TIME = self.time
        self.experience = 0
        self.diary = []

    def _load_dungeon(self, dungeon_file):
        """Загрузка подземелья из json-файла"""
        with open(file=dungeon_file, mode='r', encoding='utf-8') as file:
            dungeon = json.load(file)
            return dungeon

    def run(self):
        """Запуск приключения"""
        print(text.BACKSTORY)
        while Hero.flag:
            self._status()
            self._mobility(action_list=self._location_inspection())

    def _status(self):
        """Отображение текущего статуса героя"""
        if self.time <= 0:
            self._reborn()
        print(f'\nВы находитесь в', {self.location} if self.location else 'Вход в пещеру',
              f'\nУ вас {self.experience} опыта и осталось {self.time} до наводнения'
              f'\nПрошло {round(Hero.TIME - self.time, 2)}')

    def _reborn(self):
        """Возрождение"""
        print(text.REBORN)
        self._write_to_file()
        self.current_session = copy.deepcopy(self.dungeon)
        self.experience = 0
        self.time = Hero.TIME
        self.location = None
        self.diary = []

    def _location_inspection(self):
        """Выводит на консоль все объекты текущей локации"""
        dungeon_objects = []
        print('\nВнутри вы видите:')
        for dungeon_object in self.current_session:
            if type(dungeon_object) is dict:
                for object in dungeon_object:
                    dungeon_object = object
            current_object = self._object_type_definition(dungeon_object=dungeon_object)
            if type(current_object) is Location:
                print(f'- Вход в локацию: {current_object}')
            elif type(current_object) is Monster:
                print(f'- Монстра: {current_object}')
            elif type(current_object) is Hatch:
                print(f'- Люк: {current_object}')
            dungeon_objects.append(current_object)
        if not dungeon_objects:
            print(f'\n\tВы забрели в тупик. Вода уже на подходе!')
            self.time = 0
        return dungeon_objects

    def _mobility(self, action_list):
        """Проверяет остались ли у героя варианты действий"""
        if action_list:
            self._act(action_list)
        else:
            self._reborn()

    def _act(self, action_list):
        """Герой выполняет действие выбранное пользователем"""
        print('\nВыберите действие:')
        for i, action in enumerate(action_list):
            if type(action) is Location:
                print(f'{i + 1}) Перейти в {action}')
            elif type(action) is Monster:
                print(f'{i + 1}) Атаковать {action}')
            elif type(action) is Hatch:
                print(f'{i + 1}) Попробовать открыть {action}')
        choice = self._user_input(count=len(action_list))
        action = action_list[choice]
        if type(action) is Location:
            if not self.location:
                self.current_session = self.current_session[str(action)]
            else:
                self.current_session = self.current_session[choice][str(action)]
            self.location = str(action)
            self.time -= action.time
            print(f'\nВы выбрали переход в локацию {str(action)}')
        elif type(action) is Monster:
            del self.current_session[choice]
            self.experience += action.experience
            self.time -= action.time
            print(f'\nВы выбрали атаковать монстра {str(action)}')
        elif type(action) is Hatch:
            if self.experience >= 280:
                self.time -= action.time
                if self.time >= 0:
                    print('\tБлагодаря полученному при сражении с врагом опыту вы с легкостью разгадываете '
                          'как рабртает люк и открываете его.\n\t', self.current_session[choice][str(action)])
                    Hero.flag = False
                    self._write_to_file()
                else:
                    print(f'\n\tВы не успели открыть люк.')
                    self.time = 0
            else:
                print(f'\n\tВам не хватило боевого опыта({self.experience} < 280), чтобы разгодать как открыть, '
                      f'сооруженный монстрами люк.')
                self.time = 0
        self._make_record()

    def _make_record(self):
        """Делает новую запись о состоянии героя в дневник"""
        self.diary.append({'current_location': self.location, 'current_experience': self.experience,
                           'current_date': datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')})

    def _write_to_file(self):
        """Записывает дневник героя во внешний файл"""
        with open(file='dungeon.csv', mode='w', encoding='utf-8') as file:
            writer = csv.DictWriter(f=file, fieldnames=['current_location', 'current_experience',
                                                        'current_date'])
            writer.writeheader()
            writer.writerows(rowdicts=self.diary)

    def _user_input(self, count):
        """Ввод пользователя и проверка ввода"""
        while True:
            try:
                choice = int(input(f'{"*" * 10}:')) - 1
                if - 1 < choice <= count - 1:
                    break
                else:
                    print('Число не попадает в диапозон доступных значений')
            except ValueError:
                print('Неверный ввод!')
        return choice

    def _object_type_definition(self, dungeon_object):
        """Распознает сценарий из внешего файла и создаёт нужный игровой объект"""
        if re.fullmatch(Location.LOCATION, dungeon_object):
            dungeon_object = re.fullmatch(Location.LOCATION, dungeon_object)
            current_object = Location(dungeon_object=dungeon_object)
        elif re.fullmatch(Monster.MOB, dungeon_object):
            dungeon_object = re.fullmatch(Monster.MOB, dungeon_object)
            current_object = Monster(dungeon_object=dungeon_object)
        elif re.fullmatch(Hatch.HATCH, dungeon_object):
            dungeon_object = re.fullmatch(Hatch.HATCH, dungeon_object)
            current_object = Hatch(dungeon_object=dungeon_object)
        else:
            raise ValueError(f'Неизвестный объект, {dungeon_object}')
        return current_object


lu = Hero(name='Лу', dungeon_file='rpg.json')
lu.run()
