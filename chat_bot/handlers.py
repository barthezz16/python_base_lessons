import re

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
