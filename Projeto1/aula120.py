from dotenv import load_dotenv
import os
import locale, string
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import aula126
load_dotenv()

locale.setlocale(locale.LC_ALL, '')


#Dados remetente e destinatario
sender = os.getenv('FROM_EMAIL', '')
reciever = sender

#configuracoes do servidor smtp
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

#mensagem do email

def convert_brl(value):
    value_in_brl = 'R$' + locale.currency(val= value, grouping=True, symbol=False)
    return value_in_brl

date = datetime(2024, 10, 9)
data_ = dict(
    name= 'Name',
    date= date.strftime('%d/%m/%Y'),
    value = convert_brl(6000540.61),
    company = 'Company LLC',
    number= '607-540-890'
)

text = '''
Prezado(a) $name,

Sua transação na data de $date, no valor de $value, para a empresa $company,
foi aprovada, caso não reconheça a transação favor entre em contato com $number

'''
template = string.Template(text)
message_email = template.substitute(data_)

#transformando o texto para MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = reciever
mime_multipart['subject'] = 'Email Enviado através do Python'

#envia o email
email_body = MIMEText(message_email, 'plain', 'utf-8')
mime_multipart.attach(email_body)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email Enviado')