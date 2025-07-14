import sqlite3
import logging

def create_tables(db_path='history.db'):
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time TEXT,
                    date TEXT,
                    title TEXT,
                    image BLOB
                )
            ''')
        logging.info("Таблица requests успешно создана или уже существует.")
    except Exception as e:
        logging.error(f"Ошибка при создании таблицы: {e}")