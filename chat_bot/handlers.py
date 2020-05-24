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
        context['city_arrival'] = text.title()
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
        if context['date'] in flights[(context['city_departure'])][(context['city_arrival'])]:
            return True
        else:
            return False


def handler_flights(context, text):
    context['flights'] = flights
    pprint(context['flights'][context['city_departure']])
    if context['city_arrival'] in flights[(context['city_departure'])]:
        return True
    else:
        return False


def dates_creator():
    start_date = DT.datetime.now()
    end_date = start_date + DT.timedelta(days=30)
    number_of_flights_per_month_moscow_berlin = 8
    res_moscow_berlin = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_moscow_berlin).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_moscow_newyork = 15
    res_moscow_newyork = pd.date_range(start_date, end_date,
                                       periods=number_of_flights_per_month_moscow_newyork).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_moscow_madrid = 6
    res_moscow_madrid = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_moscow_madrid).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_berlin_madrid = 11
    res_berlin_madrid = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_berlin_madrid).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_newyork_madrid = 16
    res_newyork_madrid = pd.date_range(start_date, end_date,
                                       periods=number_of_flights_per_month_newyork_madrid).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_newyork_london = 12
    res_newyork_london = pd.date_range(start_date, end_date,
                                       periods=number_of_flights_per_month_newyork_london).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_moscow_london = 9
    res_moscow_london = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_moscow_london).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_berlin_london = 10
    res_berlin_london = pd.date_range(start_date, end_date,
                                      periods=number_of_flights_per_month_berlin_london).strftime('%d.%m.%Y').tolist()
    number_of_flights_per_month_madrid_london = 10
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
