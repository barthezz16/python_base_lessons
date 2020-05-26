from handlers import dates_creator

GROUP_ID = 194398178
TOKEN = 'aa3755f8807e08d5e1759193c1f0b59ec60c9164b5f64fe42512c9b3cce4e95429ba9ac7b197cc27f873c'

INTENTS = [
    {
        'name': 'Помощь',
        'tokens': ('\\help', 'помощь', 'как', 'что делать'),
        'scenario': None,
        'answer': 'чтобы купить билет введите \\ticket, или купить билет'
    },
    {
        'name': 'Покупка',
        'tokens': ('купить', '\\ticket', 'покуп'),
        'scenario': 'registration',
        'answer': None

    }
]

flights = dates_creator()

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Чтобы купить билет, введите город вылета.',
                'failure_text': 'Город вылета должен состоять из 3-30 букв и дефиса. Попробуйте еще раз',
                'handler': 'handler_city_departure',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите город прилета.',
                'failure_text': 'Возможно вы ввели не правильно город прилета, или совершили ошибку в названии города.'
                                '(Город прилета должен состоять из 3-30 букв и дефиса. '
                                '\n Из {city_departure} доступны рейсы в: '
                                '{flights_possible}.)',
                'handler': 'handler_city_arrival',
                'next_step': 'step3'
            },
            # 'step2.1': {
            #     'text': 'Вы ищите рейс из {city_departure} в {city_arrival}?.'
            #             '\n Пять ближайших рейсов из {city_departure} в {city_arrival}: {five_nearest}.'
            #             '\n press anykey to continue',
            #     'failure_text': 'Нет прямого рейса из {city_departure} в {city_arrival}. '
            #                     'Из {city_departure} доступны рейсы в: '
            #                     '{flights_possible}. Давайте начнем заново!',
            #     'handler': 'handler_flights',
            #     'next_step': 'step3'
            # },
            'step3': {
                'text': 'Вы ищите рейс из {city_departure} в {city_arrival}?.'
                        '\n Пять ближайших рейсов из {city_departure} в {city_arrival}: {five_nearest}.'
                        '\n\n\nВведите желаемую дату вылета в формате DD.MM.YYYY.',
                'failure_text': 'Пять ближайших рейсов из {city_departure} в {city_arrival}: '
                                '{five_nearest}.',
                'handler': 'handler_date',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Выберите желаемую дату вылета из ближайших к желаемой дате вылета {dates_list}.',
                'failure_text': 'Введите желаемую дату вылета в формате DD.MM.YYYY.',
                'handler': 'handler_date',
                'next_step': 'step5'
            },
            'step5': {
                'text': 'Выберите количество мест от 1 до 5.',
                'failure_text': 'Максиммальное количество мест 5.',
                'handler': 'handler_seats',
                'next_step': 'step6'
            },
            'step6': {
                'text': 'Введите коментарий к заказу.',
                'failure_text': 'Введите коментарий к заказу.',
                'handler': 'handler_message',
                'next_step': 'step7'
            },
            'step7': {
                'text': 'Проверьте пожалуйста введенные данные, если все верно, введите "Да".'
                        '\nГород вылета: {city_departure}. '
                        '\nГород прилета: {city_arrival}.'
                        '\nДата: {date}. '
                        '\nКоличество мест: {seats}.'
                        '\nКомментарий: {message}.',
                'failure_text': 'Вы нашли ошибку в введенных данных, давайте повторим еще раз.',
                'handler': 'handler_confirm',
                'next_step': 'step8'  # TODO restart
            },
            'step8': {
                'text': 'Введите номер телефона в формате (XXX)XXX-XX-XX.',
                'failure_text': 'Вы ввели неправильный номер, формат ввода (XXX)XXX-XX-XX, попробуйте еще раз.',
                'handler': 'handler_phone',
                'next_step': 'step9'
            },
            'step9': {
                'text': 'Спасибо за покупку, мы свяжемся с вами по указанному номеру ({phone})..',
                'failure_text': None,
                'handler': None,
                'next_step': None

            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю, как на это ответить. '
