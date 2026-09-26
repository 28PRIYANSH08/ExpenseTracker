import sqlite3
import os


PROJECT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATABASE_NAME = os.path.join(PROJECT_FOLDER, "data", "expenses.db")


def connect_database():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    