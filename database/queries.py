import sqlite3


def add_database(user_name: str, time: str, date: str, title: str, image_bytes: bytes) -> None:
    """Добавляет запись в таблицу requests с информацией о запросе и изображении.

        :param user_name: Имя пользователя, сделавшего запрос.
        :param time: Время запроса в формате строки.
        :param date: Дата изображения.
        :param title: Заголовок изображения.
        :param image_bytes: Данные изображения в байтах.
    """
    if image_bytes is None:
        image_bytes = b''
    with sqlite3.connect('history.db') as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO requests (user_name, time, date_image, title, image)
                    VALUES (?, ?, ?, ?, ?)''', (user_name, time, date, title, sqlite3.Binary(image_bytes)))