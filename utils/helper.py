from datetime import date
from datetime import datetime


def date_to_str(informed_date: date) -> str:
    return informed_date.strftime('%d/%m/%Y')


def str_to_date(informed_date: str) -> date:
    return datetime.strptime(informed_date, '%d/%m/%Y')


def float_to_str_currency(value: float) -> str:
    return f'R$ {value:,.2f}'
