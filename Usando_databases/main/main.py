import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE = 'costumers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
   f'CREATE TABLE IF NOT EXISTS {TABLE}'
   '('
   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
   'name TEXT,'
   'weight REAL'
   ')'
)
connection.commit()

cursor.execute(f'DELETE FROM {TABLE}')
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE}"')
connection.commit()

sql_insert = (f'INSERT INTO {TABLE} (name, weight)'
               'VALUES'
               '(?, ?)')

sql_insert_dict = (f'INSERT INTO {TABLE} (name, weight)'
               'VALUES'
               '(:name, :weight)')

# cursor.execute(sql_insert, ['Jones', 78.6])
cursor.executemany(sql_insert, [['Jones', 10], ['Smith', 79.7], ['Java', 1000]])
connection.commit()

cursor.executemany(sql_insert_dict,[ 
                   {'name': 'Nri', 'weight': 45}, 
                   {'name': 'Nuri', 'weight': 55},
                   ])
connection.commit()

cursor.close()
connection.close()