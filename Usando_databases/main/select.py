import sqlite3
from main import DB_FILE, TABLE # type: ignore

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

def query():
    
    print('id name weight')

    for i in range(0,6):
        cursor.execute(f'SELECT * FROM {TABLE} LIMIT {i}, 1'
                )
        
        for row in cursor.fetchall():
            _id, name, weight = row

            print(str(_id), name, str(weight))

if __name__ == '__main__':
    query()

cursor.close()
connection.close()

# cursor.execute(f'DELETE FROM {TABLE}'
#                 'WHERE id = 2'            
# )

# cursor.execute(f'UPDATE {TABLE} '
#                 'SET name="A" '
#                 'WHERE id = 2')