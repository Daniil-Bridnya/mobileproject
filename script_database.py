import sqlite3

goods = [
    [1, 'Mortal Kombat 1', 'Игра на компанию', 'файтинг', 8, 60, 190],
    [2, 'Hi-Fi Rush', 'приключение, для одного игрока', 'слешер', 9, 120, 34],
    [3, 'Sea of Stars', 'приключение, для одного игрока', 'RPG', 6, 45, 300],
    [4, 'Amnesia: The Bunker', 'приключение, острый сюжет', 'хоррор', 8, 120, 54],
    [5, 'Resident Evil 4', 'переиздание, классика', 'хоррор', 10, 120, 22],
    [6, 'Cyberpunk 2077', 'популярная игра, будущее', 'RPG', 10, 120, 15],
]


connection = sqlite3.connect('instance/goods.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS goods (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
tags TEXT NOT NULL,
user_evaluation INTEGER ,
price INTEGER NOT NULL,
stock_balance INTEGER NOT NULL
)
''')
connection.commit()
connection.close()

for good in goods:
    connection = sqlite3.connect('instance/goods.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO goods (title, description, tags, user_evaluation, price, stock_balance)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                   (good[1], good[2], good[3], good[4], good[5], good[6]))
    connection.commit()
    connection.close()
