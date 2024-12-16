import sqlite3
import requests


def get_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    return r.json()


def insert_posts():
    for element in get_posts():
        cursor.execute(
            'INSERT OR REPLACE INTO posts (user_id,id,title,body) VALUES(?,?,?,?)',
            (element["userId"], element["id"], element["title"], element["body"])
        )


def view_all_posts():
    # Выбираем всех пользователей
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()

    # Выводим результаты
    for post in posts:
        print(post)


def view_user_posts(userid):
    # Выбираем посты одного пользователя
    cursor.execute('SELECT * FROM posts WHERE user_id=?', (userid,))
    posts = cursor.fetchall()

    # Выводим результаты
    for post in posts:
        print(post)


# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу posts
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
id INTEGER PRIMARY KEY,
user_id integer,
title TEXT,
body TEXT 
)'''
               )

insert_posts()
view_all_posts()
view_user_posts(4)
# выравнивание ctrl+alt+L
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
