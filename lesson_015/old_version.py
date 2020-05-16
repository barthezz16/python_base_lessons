import csv
import json
import re
from datetime import datetime, timedelta
from decimal import Decimal
from pprint import pprint


class DungeonGame:

    def __init__(self):
        self.re_location = r'\w+_\w*(\d+)_tm(\d+).*\d+'
        #  тут не понятно, почему эта регулярка не ловит
        #  'Hatch_tm159.098765432'
        self.re_mobs = r'\w+_exp(\d+)_tm(\d+)'
        self.current_location_name = "Location_0_tm0"
        self.re_exit = r'Hatch_tm159.098765432'
        self.location = data["Location_0_tm0"]
        self.mob_list = []
        self.location_list = []
        self.exp = 0
        self.time_elapsed = datetime.strptime('00:00', '%M:%S')
        self.remaining_time = '123456.0987654321'
        self.choice = None

    def run(self, start_location):
        if self.current_location_name == 'Hatch_tm159.098765432':
            print('Поздравляю!!! ВЫ ПОБЕДИТЕЛЬ!!!')
            self.writer()
        else:
            if Decimal(self.remaining_time) > 0:
                self.print_and_data_check(start_location)
                self.make_a_choice()
                self.writer()
            else:
                print('В этот раз не получилось, вы возвращаетесь в начало')
                self.remaining_time = '123456.0987654321'
                self.run(start_location=data["Location_0_tm0"])
                self.time_elapsed = datetime.strptime('00:00', '%M:%S')
                self.writer()

    def writer(self):
        result = [{'current_location': self.current_location_name,
                   'current_experience': self.exp,
                   'current_date': str(self.time_elapsed.time())
                   }
                  ]

        with open('result.csv', 'a', encoding='utf8') as result_file:
            writer = csv.DictWriter(result_file, fieldnames=['current_location', 'current_experience', 'current_date'])
            writer.writerows(result)

    def print_and_data_check(self, location):
        self.location_list = []
        self.mob_list = []
        print(f'Вы находитесь в', self.current_location_name)
        print(f'У вас {self.exp} опыта и осталось {self.remaining_time} секунд до наводнения')
        print(f'Прошло времени: {self.time_elapsed.time()}')
        print('Внутри вы видите:')
        for key, item in enumerate(location):
            self.mob_list_update(item)
            self.location_list_update(item, key)
        print('Выберите действие:')
        self.choose_action()
        return location

    def location_list_update(self, item, key):
        if isinstance(item, dict):
            self.location_list.append((list(item.keys())[0], key))
            print('— Вход в локацию:', self.location_list[-1][0])

    def mob_list_update(self, item):
        if isinstance(item, str):
            self.mob_list.append(item)
            print('— Монстра: ', item)

    def choose_action(self):
        self.input()
        if int(self.choice) > 3:
            print('Введено непрвильное значение попоробуйте еще раз! ')
            self.choose_action()
        else:
            if int(self.choice) == 1 and len(self.mob_list) > 0:
                if len(self.mob_list) > 0:
                    print(f'Похвально, вы выбрали бой!'
                          f'\n!!!Ну что-же начнем!!!')
                    for key, monster_name in enumerate(self.mob_list, start=1):
                        print(f'Атаковать монстра {key} {monster_name}')
            elif int(self.choice) == 1 and len(self.mob_list) == 0:
                print('Локация полностью зачищенна!')
                self.make_a_choice()
                #  Нужно уходить от рекурсии в пользу цикла
                #  Обернуть выбор действия в цикл - тогда тут, если локация зачищена просто
                #  начнётся запрос нового выбора
                # Вот где проблема. Рекурсия, которой стоит избегать, показала своё лицо)
                #  Выбирая действие "на локции нет монстров" мы запускаем рекурсию
                #  выбираем новый self.choice = 2, распечатываем все локации
                #  Затем продолжается текущий метод, из которого вызван был self.choose_action()
                #  Он выполняет следующую проверку if int(self.choice) == 2:
                #  И опять распечатывает локации)
                #  я видел эту проблему, пока не нашел решение к ней
        if int(self.choice) == 2:
            for key, location_name in enumerate(self.location_list, start=1):
                print(f'Перейти в локацию {key} {location_name[0]}')
        elif int(self.choice) == 3:
            self.exit()

    def input(self):
        if len(self.mob_list) > 0:
            self.choice = input('1) Атаковать монстров на локации. '
                                '\n2) Переход в другую локацию. '
                                '\n3) Сдаться и выйти из игры! ')
        else:
            self.choice = input('1) На локации нет монстров! '
                                '\n2) Переход в другую локацию. '
                                '\n3) Сдаться и выйти из игры! ')

    def make_a_choice(self):
        while not self.choice.isdigit() or len(self.choice) > 2:
            self.choice = input('Введено непрвильное значение попоробуйте еще раз! ')
        if int(self.choice) == 3:
            pass
        else:
            if int(self.choice) == 1:
                self.kill_mob()
                self.choose_action()
                #  Причина тут
                #  После убийтсва моба запускается выбор действия
                #  И, при выборе 1, если есть мобы, которые живы, функция просто печатает их
                #  И больше ничего не делает.
                #  Если же после убийства мобов не остаётся - вызывается та ваша рекурсия
                #  В идеале было бы чтобы только один метод вызывал другие
                #  А то выходит всё запутаннее и запутаннее :)
                #  Впору рисовать все зависимости и ходы на бумаге
            if int(self.choice) == 2:
                self.location_change()

    def location_change(self):
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
        print(f'У вас {self.exp} опыта и осталось {self.remaining_time} секунд до наводнения')
        print(f'Прошло времени: {self.time_elapsed.time()}')
        self.writer()
        self.run(start_location=self.location)

    def kill_mob(self):
        choice_to_kill = input('Выберите монстра для атаки. ')
        while int(choice_to_kill) > len(self.mob_list):
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


with open('rpg.json', 'r', encoding='utf8') as file_with_data:
    data = json.load(file_with_data)

with open('result.csv', 'w', encoding='utf8') as result_file:
    writer = csv.DictWriter(result_file, fieldnames=['current_location', 'current_experience', 'current_date'])
    writer.writeheader()

field_names = ['current_location', 'current_experience', 'current_date']
start_location = data["Location_0_tm0"]
start_game = DungeonGame()
start_game.run(start_location=start_location)
