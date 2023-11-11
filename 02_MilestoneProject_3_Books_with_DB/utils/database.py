# import sqlite3
from typing import List, Dict, Union
from .database_connection import DatabaseConnection
"""
Concerned with storing and retrieving books from a database.
"""


def create_book_table() -> None:
    # connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    # connection.commit()
    # connection.close()


def add_book(name: str, author: str) -> None:
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
    # cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    # connection.commit()
    # connection.close()


def get_all_books() -> List[Dict[str, Union[str, int]]]:

    try:
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM books')
        # connection.commit()
            books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        # returns list of tuples [(name, author, read), (..,..,..)]

        # connection.close()

        print(books)

        return books

    except FileNotFoundError:
        print("There are no books ATM.")
        create_book_table()


def mark_book_as_read(book_read: str) -> None:
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (book_read,))
    # connection.commit()
    # connection.close()


def delete_book(book_to_delete: str) -> None:
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (book_to_delete,))
    # connection.commit()
    # connection.close()

