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
    # TODO перед распределением на три переменные стоит проверить размер получившегося списка
    # TODO И вызвать исключение, если элементов не хватает
    name, email, age = line.split(' ')
    age = int(age)
    if not name.isalpha:  # TODO Тут вы просто забыли "()" добавить к isalpha
        # все остальные проверки вроде работают, но тут иногда проскакиваю имена с цифрами
        # не совсем понимаю почему...
        raise NotNameError
    elif '.' not in email and '@' not in email:
        raise NotEmailError
    elif not 10 < age < 99:
        raise ValueError(' поле возраст НЕ является числом от 10 до 99')
    return name, email, age


with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            name, email, age = registration_check(line)
            good_log_file = 'registrations_good.log'
            file = open(good_log_file, mode='a', encoding='utf8')
            # TODO Почему бы открытие и закрытие файла
            # TODO не вынести за пределы цикла?
            log_content = f'{name} {email} {age} \n'
            file.write(str(log_content))
            file.close()
        except Exception as exc:
            bad_log_file = 'registrations_bad.log'
            file = open(bad_log_file, mode='a', encoding='utf8')
            log_content = line + str(exc) + '\n'
            file.write(str(log_content))
            file.close()
