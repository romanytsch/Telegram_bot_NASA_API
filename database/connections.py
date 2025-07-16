import sqlite3
import logging

def create_tables(db_path: str = 'history.db') -> None:
    """Создаёт таблицу requests в базе, если её нет.

        :param db_path: Путь к файлу базы данных.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT,
                    time TEXT,
                    date_image TEXT,
                    title TEXT,
                    image BLOB
                )
            ''')
        logging.info("Таблица requests успешно создана или уже существует.")
    except Exception as e:
        logging.error(f"Ошибка при создании таблицы: {e}")