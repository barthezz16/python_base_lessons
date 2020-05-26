import datetime as DT
from pprint import pprint

import pandas as pd


def handler_flights(departure, arrival):
    if arrival in flights[departure]:
        return f'Пять ближайших рейсов из {dep_i} в {arr_i}: {", ".join(map(str, flights[departure][arrival][0: 5]))}.'

    else:
        return f'Нет прямого рейса из {departure} в {arrival}. Из {departure} доступны рейсы в: ' \
               f'{", ".join(map(str, flights[departure].keys()))}.'


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

    my_date = DT.datetime.strptime('12.10.2020', '%d.%m.%Y')
    while not my_date.strftime('%d.%m.%Y') in res_moscow_berlin:
        try:
            my_date_index = res_moscow_berlin.index(my_date)
        except ValueError:
            my_date += DT.timedelta(days=1)
            print(my_date.strftime('%d.%m.%Y'))
    my_date_index = res_moscow_berlin.index(my_date.strftime('%d.%m.%Y'))
    dates_list = res_moscow_berlin[my_date_index: my_date_index + 5]
    print(dates_list)
    pprint(res_moscow_berlin)

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
departure = ['Moscow', 'Berlin', 'Madrid', 'New-York', 'London']
arrival_list = ['Moscow', 'Berlin', 'Madrid', 'New-York', 'London']
for dep_i in departure:
    for arr_i in arrival_list:
        if dep_i == arr_i:
            pass
        else:
            try:
                result = handler_flights(departure=dep_i.title(), arrival=arr_i.title())
                # print(result)
            except KeyError:
                print('Из данного города нет рейсов')
