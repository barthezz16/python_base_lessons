# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):

    def __str__(self):
        return ' поле имени содержит НЕ только буквы'


class NotEmailError(Exception):

    def __str__(self):
        return ' поле емейл НЕ содержит @ и .(точку)'


def registration_check(line):
    if len(line.split(' ')) < 3:
        raise ValueError(' НЕ хватает элементов!')
    name, email, age = line.split(' ')
    age = int(age)
    if not name.isalpha():
        raise NotNameError
    elif '.' not in email and '@' not in email:
        raise NotEmailError
    elif not 10 <= age <= 99:
        raise ValueError(' поле возраст НЕ является числом от 10 до 99')
    return name, email, age


with open('registrations.txt', 'r', encoding='utf8') as ff:
    good_log_file = 'registrations_good.log'
    with open(good_log_file, mode='a', encoding='utf8') as good_file:
        bad_log_file = 'registrations_bad.log'
        with open(bad_log_file, mode='a', encoding='utf8') as bad_file:
            for line in ff:
                line = line[:-1]
                try:
                    name, email, age = registration_check(line)
                    log_content = f'{name:<10} {email:<20} {age:<3} \n'
                    good_file.write(str(log_content))
                except Exception as exc:
                    log_content = line + str(exc) + '\n'
                    bad_file.write(str(log_content))
