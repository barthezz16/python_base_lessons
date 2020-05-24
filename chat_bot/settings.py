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
                'failure_text': 'Город прилета должен состоять из 3-30 букв и дефиса. Попробуйте еще раз.',
                'handler': 'handler_city_arrival',
                'next_step': 'step2.1'
            },
            'step2.1': {
                'text': 'Вы ищите рейс из из {city_departure} в {city_arrival}.',
                'failure_text': 'Нет прямого рейса из {city_departure} в {city_arrival}. '
                                'Из {city_departure} доступны рейсы в: '
                                '{", ".join(map(str, flights))}.',  # TODO врое через какието костыли запихнул список сюда
                # TODO но получается вызвать только весь список, с ключами беда какая то...
                # TODO или я все таки не правльно это сделал...
                'handler': 'handler_flights',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Введите дату вылета в формате MM-DD-YYYY.',
                'failure_text': 'Пять ближайших рейсов из {city_departure} в {city_arrival}: '
                                '{", ".join(map(str, flights[context["city_departure"]][context["city_arrival"]]'
                                '[0: 5]))}.',  # не пойму как это заставить тут работать...
                'handler': 'handler_date',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Выберите подходящий вам рейс.',
                'failure_text': 'Вы ввели неправильный номер. Введите номер рейса от 1 до 5.',
                'handler': 'handler_digit',
                'next_step': 'step5'
            },
            'step5': {
                'text': 'Выберите количество мест от 1 до 5.',
                'failure_text': 'Вы ввели неправильный номер. Введите количество мест от 1 до 5.',
                'handler': 'handler_digit',
                'next_step': 'step6'
            },
            'step6': {
                'text': 'Введиет коментарий к заказу.',
                'failure_text': 'Введиет коментарий к заказу.',
                'handler': 'handler_message',
                'next_step': 'step7'
            },
            'step7': {
                'text': 'Проверьте пожалуйста введенные данные, если все верно, введите "Да".',
                'failure_text': 'Вы нашли ошибку в введенных данных, давайте повторим еще раз.',
                'handler': 'handler_message',
                'next_step': 'step8'
            },
            'step8': {
                'text': 'Введите номер телефона в формате (XXX)XXX-XX-XX.',
                'failure_text': 'Вы ввели неправильный номер, формат ввода (XXX)XXX-XX-XX, попробуйте еще раз.',
                'handler': 'handler_phone',
                'next_step': 'step9'
            },
            'step9': {
                'text': 'Спасибо за покупку, мы свяжемся с вами по указанному номеру ({phone})..',
                'failure_text': 'Спасибо за покупку, мы свяжемся с вами по указанному номеру ({phone})..',
                'handler': None,
                'next_step': None

            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю, как на это ответить. '
