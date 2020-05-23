import datetime as DT
import pandas as pd


def handler_flights(departure, arrival):
    if arrival in flights[departure]:
        return f'Пять ближайших рейсов из {dep_i} в {arr_i}: {", ".join(map(str, flights[departure][arrival][0: 5]))}.'

    else:
        return f'Нет прямого рейса из {departure} в {arrival}. Из {departure} доступны рейсы в: ' \
               f'{", ".join(map(str, flights[departure].keys()))}.'


def dates_creator():
    global flights
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


dates_creator()
departure = ['Moscow', 'Berlin', 'Madrid', 'New-York', 'London']
arrival_list = ['Moscow', 'Berlin', 'Madrid', 'New-York', 'London']
for dep_i in departure:
    for arr_i in arrival_list:
        if dep_i == arr_i:
            pass
        else:
            try:
                result = handler_flights(departure=dep_i.title(), arrival=arr_i.title())
                print(result)
            except KeyError:
                print('Из данного города нет рейсов')
