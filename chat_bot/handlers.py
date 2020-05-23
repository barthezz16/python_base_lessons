import re
import datetime as DT
import pandas as pd

re_city = re.compile(r'^(?ix)^[A-Z.-]+(?:\s+[A-Z.-]+)*$')
re_date = re.compile(r'\b\d+.\d+.\d+\b')
re_phone = re.compile(r'\b\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}\b')
re_message = re.compile(r'\w+')
re_digit = re.compile(r'[1-5]')


def handler_city_departure(text, context):
    matches = re.match(re_city, text)
    if matches:
        context['city_departure'] = text
        return True
    else:
        return False


def handler_message(text, context):
    matches = re.match(re_message, text)
    if matches:
        context['message'] = text
        return True
    else:
        return False


def handler_digit(text, context):
    matches = re.match(re_digit, text)
    if matches:
        context['digit'] = text
        return True
    else:
        return False


def handler_city_arrival(text, context):
    matches = re.match(re_city, text)
    if matches:
        context['city_arrival'] = text
        return True
    else:
        return False


def handler_phone(text, context):
    matches = re.findall(re_phone, text)
    if len(matches) > 0:
        context['phone'] = matches[0]
        return True
    else:
        return False


def handler_date(text, context):
    matches = re.findall(re_date, text)
    if len(matches) > 0:
        context['date'] = matches[0]
        return True
    else:
        return False


def handler_flights(context, *args, **kwargs):  # TODO Handler вызывается с двумя параметрами - text/context
    # TODO Нужно их и записать, как в остальных
    global flights
    print(context['city_arrival'])
    print(context['city_departure'])
    if context['city_departure'] in flights[context['city_arrival']]:
        return True
    else:
        return False


# TODO Это создание хорошо бы в функцию убрать
start_date = DT.datetime.now()
end_date = start_date + DT.timedelta(days=30)

number_of_flights_per_mounth_moscow_berlin = 8
res_moscow_berlin = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                  # TODO Ещё не понимаю зачем тут нужны min/max?
                                  periods=number_of_flights_per_mounth_moscow_berlin).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_moscow_newyork = 15
res_moscow_newyork = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                   periods=number_of_flights_per_mounth_moscow_newyork).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_moscow_madrid = 6
res_moscow_madrid = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                  periods=number_of_flights_per_mounth_moscow_madrid).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_berlin_madrid = 11
res_berlin_madrid = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                  periods=number_of_flights_per_mounth_berlin_madrid).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_newyork_madrid = 16
res_newyork_madrid = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                   periods=number_of_flights_per_mounth_newyork_madrid).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_newyork_london = 12
res_newyork_london = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                   periods=number_of_flights_per_mounth_newyork_london).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_moscow_london = 9
res_moscow_london = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                  periods=number_of_flights_per_mounth_moscow_london).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_berlin_london = 10
res_berlin_london = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                  periods=number_of_flights_per_mounth_berlin_london).strftime('%d.%m.%Y').tolist()
number_of_flights_per_mounth_madrid_london = 10
res_madrid_london = pd.date_range(min(start_date, end_date), max(start_date, end_date),
                                  periods=number_of_flights_per_mounth_madrid_london).strftime('%d.%m.%Y').tolist()
# TODO И стоит это автоматизировать при помощи циклов
# TODO Создать заранее список городов и начальную/конечную даты
# TODO И циклом сформировать подобный словарь.
flights = {
    'Moscow': {
        'Berlin': res_moscow_berlin,
        'Madrid': res_moscow_madrid,
        'New-York': res_moscow_newyork,
        'London': res_moscow_london
    },
    'Berlin': {
        'Moscow': res_moscow_berlin,
        'Madrid': res_berlin_madrid,
        'London': res_berlin_london

    },
    'Madrid': {
        'Moscow': res_moscow_madrid,
        'Berlin': res_berlin_madrid,
        'New-York': res_newyork_madrid,
        'London': res_madrid_london

    },
    'New-York': {
        'Moscow': res_moscow_newyork,
        'Madrid': res_newyork_madrid,
        'London': res_newyork_london
    },
    'London': {
        'Moscow': res_moscow_london,
        'Berlin': res_moscow_london,
        'New-York': res_newyork_london,
        'Madrid': res_madrid_london
    }
}

