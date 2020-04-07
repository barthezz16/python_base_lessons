# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(func):
    # TODO Тут нужно ещё одну новую функцию задать через def с параметрами *args, **kwargs
    # TODO В этой функции уже добавить написанный вами код
    bad_log_file = 'registrations_bad.log'
    with open(bad_log_file, mode='a', encoding='utf8') as registrations_bad:
        try:
            func()  # TODO сюда передавать параметры *args, **kwargs
        except Exception as exc:
                log_content = str(exc) + '\n'  # и тут тожк ступор...
                # TODO имя функции - функция.__name__
                # TODO параметры - args, kwargs
                # TODO тип ошибки - type(exc)
                # TODO текст ошибки - exc.args
                registrations_bad.write(str(log_content))
        return func  # TODO А возвращать уже не эту функцию, а новую, созданную выше (только отступ другой будет у ретурна)


# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)



# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

