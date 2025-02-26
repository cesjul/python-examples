# try, except, else, finally

try:
    a = 3
    b = 'a'
    c = a / b
    raise NameError('erro')
except ZeroDivisionError:
    print('Divisao por zero')
except TypeError as error:
    print(error.__class__.__name__, error)
finally:
    print('acabou')

