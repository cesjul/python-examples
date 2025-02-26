import pymysql
import dotenv
import os
import random
import secrets
import string

import pymysql.cursors

dotenv.load_dotenv()

connecttion = pymysql.connect(
    host = os.environ['MYSQL_HOST'],
    user= os.environ['MYSQL_USER'],
    password= os.environ['MYSQL_PASSWORD'], 
    database= os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor,
)


with connecttion:
    with connecttion.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS users ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(255) NOT NULL , '
            'age INT NOT NULL , '
            'PRIMARY KEY (id) '
            ') '
        )
        cursor.execute('TRUNCATE TABLE users')

    connecttion.commit()
        
    with connecttion.cursor() as cursor:
        sql_insert = (
            'INSERT INTO users (name, age) '
            'VALUES '
            '(%s, %s) '
        )
        cursor.execute(sql_insert, ['Julio', 21])
    connecttion.commit()

    with connecttion.cursor() as cursor:
        sql_insert_1 = (
            'INSERT INTO users (name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '  
        )

        data = {'name': 'Yasmin', 'age': 19}

        cursor.execute(sql_insert_1, data)
    connecttion.commit()

    with connecttion.cursor() as cursor:
        sql_insert_1 = (
            'INSERT INTO users (name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '  
        )

        alphabet = string.ascii_letters
        rand_times = random.randint(4, 16)
        list_ = []
        rand_range = range(random.randint(1, 6000))
        
        for i in rand_range:
            
            list_.append({'name': ''.join(secrets.choice(alphabet)
                          for i in range(rand_times)), 
                         'age': random.randint(18, 90)},
                         )
    
        data = list_

        cursor.executemany(sql_insert_1, data)
    connecttion.commit()

    with connecttion.cursor() as cursor:
        cursor.execute('SELECT * FROM users '
                       
        )
        for row in cursor.fetchall():
            print(row)
                
       


    connecttion.commit()