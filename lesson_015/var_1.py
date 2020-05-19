# -*- coding: utf-8 -*-

import csv
import datetime
import json
import re
from decimal import *


class Rpg:

    def __init__(self, json_file):
        self.json_file = json_file
        self.dictionary = None
        self.options_for_action = []
        self.experience = 0
        self.remaining_time = Decimal('123456.0987654321')
        self.current_time = datetime.datetime.now()
        self.re_time = r'\w+\d*_tm(\d+\.?\d*)'
        self.re_location = r'Location_(\w*\d+)_tm(\d+)'
        self.day = self.current_time.strftime("_%d_%m")
        self.game_count = 0

    def json_processing(self):
        with open(self.json_file, 'r', encoding='utf8') as json_data:
            self.dictionary = json.load(json_data)

    def create_csv(self):
        fields_names = ['current_location', 'current_experience', 'current_date']
        with open(f'dungeon{self.game_count}{self.day}.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerow(fields_names)

    def choose_action(self, data):
        print(f"\nУ вас осталось времени {self.remaining_time}")
        print(f'Ваш текущий уровень уровень {self.experience}\n')
        print('Выберите действие:')
        for number, option in enumerate(data):
            if isinstance(option, dict):
                y = str(*option.keys())
                print(f'{number}. Перейти в {y}')
            else:
                print(f'{number}. Убить {option}')

    def show_options(self, dictionary):
        for key, data in dictionary.items():
            location = re.search(self.re_location, key)
            print(f'\nВы находитесь в Локации {location[1]}', f'Время ее прохождения {location[2]}', sep='\n')
            print('Внутри вы видите:')
            for number, option in enumerate(data):
                if isinstance(option, dict):
                    y = str(*option.keys())
                    print(f'- {y}')
                else:
                    print(f'- {option}')
                self.options_for_action.append(option)
            self.choose_action(data)

    def counting_experience_points(self, choice):
        re_monster = r'Mob_exp(\d+)_tm(\d+)'
        re_boss = r'Boss\d*_exp(\d+)_tm(\d+)'
        monster = re.search(re_monster, choice)
        boss = re.search(re_boss, choice)
        if boss is not None:
            exp = boss[1]
        else:
            exp = monster[1]
        self.experience += int(exp)

    def countdown(self, choice):
        time = re.search(self.re_time, choice)
        time_spent = Decimal(time[1])
        self.remaining_time -= time_spent

    def writing_in_csv(self, choice):
        with open(f'dungeon{self.game_count}{self.day}.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            location = re.search(self.re_location, choice)
            if choice == 'Hatch_tm159.098765432':
                data = [choice, self.experience, self.current_time.strftime("%d.%m.%y")]
            else:
                data = [f'Location {location[1]}', self.experience, self.current_time.strftime("%d.%m.%y")]
            writer.writerow(data)
            data.clear()

    def input_validation(self, user_input):
        number_of_options = len(self.options_for_action)
        while len(user_input) != 1 or ord(user_input) not in range(48, 58) \
                or int(user_input) not in range(number_of_options):
            print(f'Вы ввели неверное значение! Введите число, от 0 до {number_of_options - 1}')
            user_input = input('Ваш выбор: ')
        return int(user_input)

    def game(self):
        if len(self.options_for_action) == 0:
            print('===== Вы проиграли =====',
                  'Вы зашли в тупик, выхода нету =(',
                  f'Пещеру затопило...', sep='\n')
            return False
        user_input = input('Ваш выбор: ')
        user_input = self.input_validation(user_input)
        choice = self.options_for_action[user_input]
        if isinstance(choice, dict):
            user_choice = str(*choice.keys())
            if user_choice == 'Hatch_tm159.098765432':
                self.countdown(user_choice)
                if self.experience >= 280 and self.remaining_time > 0:
                    print('===== Победа! =====')
                    print(f'Оставшееся время {self.remaining_time.quantize(Decimal("1.000"), ROUND_HALF_EVEN)}, '
                          f'Полученный опыт {self.experience}')
                elif len(self.options_for_action) > 1:
                    print('Недостаточно опыта, чтобы войти',
                          f'Необходимо 280, а ваш текущий уровень {self.experience}', sep='\n')
                    return True
                else:
                    print('===== Вы проиграли =====',
                          f'Ваш текущий уровень {self.experience}',
                          f'Оставшееся время {self.remaining_time}', sep='\n')
                self.writing_in_csv(user_choice)
                return False
            self.writing_in_csv(user_choice)
            self.countdown(user_choice)
            self.show_options(choice)
            self.options_for_action = list(*choice.values())
        else:
            self.countdown(choice)
            self.counting_experience_points(choice)
            self.options_for_action.pop(user_input)
            self.choose_action(self.options_for_action)
        return True

    def run(self):
        new_game = 'yes'
        while new_game == 'yes':
            self.create_csv()
            self.json_processing()
            self.remaining_time = Decimal('123456.0987654321')
            self.options_for_action = []
            self.experience = 0
            self.show_options(self.dictionary)
            x = True
            while x is True:
                x = self.game()
            else:
                self.game_count += 1
                print('Хотите начать новую игру?')
                new_game = input('Yes / No: ').lower()


rpg_json = 'rpg.json'
game = Rpg(rpg_json)
game.run()
