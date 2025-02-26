import locale, string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')

def convert_brl(value):
    value_in_brl = 'R$' + locale.currency(val= value, grouping=True, symbol=False)
    return value_in_brl

date = datetime(2024, 10, 9)
data_ = dict(
    name= 'Julio',
    date= date.strftime('%d/%m/%Y'),
    value = convert_brl(6000540.61),
    company = 'Trendy LLC',
    number= '607-540-890'
)

text = '''
Prezado(a) $name,

Sua transação na data de $date, no valor de $value, para a empresa $company,
foi aprovada, caso não reconheça a transação favor entre em contato com $number

'''

template = string.Template(text)
print(template.substitute(data_))

