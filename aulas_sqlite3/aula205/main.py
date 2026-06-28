import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

#registrar valores nas colunas da tabela
sql = ( 
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight)' 
    'VALUES'
    '(:name, :weight)'
    )
# cursor.execute(sql, ["Nemisco Sapequisco", 14.2])
# cursor.executemany(
#     sql, 
#     [
#         ["Nemisco gatisco", 14.2],
#         ["Nemisco mordisco", 16.2], 
#         ["Nemisco laranjinha", 14.2] 
#     ]
# )

# cursor.execute(sql, {"name":"Nemisco Titisco", 'weight': 14.2})
# cursor.executemany(
#     sql, 
#     (
#         {"name":"Nemisco lindisco", 'weight':16.2},
#         {"name":"Nemisco inteligentisco", 'weight':11.2}, 
#         {"name":"Nemisco fofisco", 'weight':15.2}
#     )
# )

connection.commit()

if __name__  == '__main__':
    print(sql)

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    
    connection.commit()
    
    
    cursor.close() 
    connection.close()
#DELETE SEM WHERE
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# connection.commit()

# DELETE DE IDs
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"'
# )
# connection.commit()



