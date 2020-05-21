import re

re_city = re.compile(r'^(?ix)^[A-Z.-]+(?:\s+[A-Z.-]+)*$')
re_date = re.compile(r'\b\d+.\d+.\d+\b')
re_phone = re.compile(r'\b\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}\b')


def handler_city(text, context):
    matches = re.match(re_city, text)
    if matches:
        context['city'] = text
        return True
    else:
        return False


def handler_phone(text, context):
    matches = re.findall(re_date, text)
    if len(matches) > 0:
        context['phone'] = matches[0]
        return True
    else:
        return False
