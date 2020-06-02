import re
import datetime as DT
from pprint import pprint

import pandas as pd

re_city = re.compile(r'^(?ix)^[A-Z.-]+(?:\s+[A-Z.-]+)*$')
re_date = re.compile(r'\b\d+.\d+.\d+\b')
re_phone = re.compile(r'\b\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}\b')
re_message = re.compile(r'\w+')
re_digit = re.compile(r'[1-5]')


def handler_city_departure(text, context):
    matches = re.match(re_city, text)
    if matches:
        context['city_departure'] = text.title()
        if context['city_departure'] in flights:
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


def handler_confirm(text, context):
    context['confirmation'] = text
    confirm_answers = ['Да', 'да', 'ok', 'Ok', 'Yes', 'yes']
    if context['confirmation'] in confirm_answers:
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


def handler_seats(text, context):
    matches = re.match(re_digit, text)
    if matches:
        context['seats'] = text
        return True
    else:
        return False


def handler_city_arrival(text, context):
    matches = re.match(re_city, text)
    context['city_arrival'] = text.title()
    context['flights'] = flights
    context['flights_possible'] = {", ".join(map(str, context['flights'][context['city_departure']].keys()))}

    if matches and context['city_arrival'] in flights[(context['city_departure'])]:
        context['five_nearest'] = flights[context['city_departure']][context['city_arrival']][0: 5]
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
        my_date = DT.datetime.strptime(context['date'], '%d.%m.%Y')
        while not my_date.strftime('%d.%m.%Y') in flights[context['city_departure']][context['city_arrival']]:
            try:
                my_date_index = flights[context['city_departure']][context['city_arrival']].index(my_date)
            except ValueError:
                my_date += DT.timedelta(days=1)
                # print(my_date.strftime('%d.%m.%Y'))
        my_date_index = flights[context['city_departure']][context['city_arrival']].index(my_date.strftime('%d.%m.%Y'))
        context['dates_list'] = flights[context['city_departure']][context['city_arrival']][
                                my_date_index: my_date_index + 5]
        if context['date'] in flights[(context['city_departure'])][(context['city_arrival'])]:
            return True
        else:
            return False


def handler_flights(context, text):
    context['flights_possible'] = {", ".join(map(str, context['flights'][context['city_departure']].keys()))}
    if context['city_arrival'] in flights[(context['city_departure'])]:
        return True
    else:
        return False


def dates_creator():
    start_date = DT.datetime.now()
    end_date = start_date + DT.timedelta(days=365)
    number_of_flights_per_month_moscow_berlin = 80
    res_moscow_berlin = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_moscow_berlin).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_moscow_newyork = 180
    res_moscow_newyork = pd.date_range(start_date, end_date,
                                       periods=number_of_flights_per_month_moscow_newyork).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_moscow_madrid = 75
    res_moscow_madrid = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_moscow_madrid).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_berlin_madrid = 135
    res_berlin_madrid = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_berlin_madrid).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_newyork_madrid = 185
    res_newyork_madrid = pd.date_range(start_date, end_date,
                                       periods=number_of_flights_per_month_newyork_madrid).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_newyork_london = 145
    res_newyork_london = pd.date_range(start_date, end_date,
                                       periods=number_of_flights_per_month_newyork_london).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_moscow_london = 110
    res_moscow_london = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_moscow_london).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_berlin_london = 120
    res_berlin_london = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_berlin_london).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_madrid_london = 125
    res_madrid_london = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_madrid_london).strftime('%d.%m.%Y').tolist()
    flights_list = {
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
    return flights_list


flights = dates_creator()
