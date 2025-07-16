from io import BytesIO

from loader import bot
from telebot.types import Message
import sqlite3


@bot.message_handler(commands=["history"])
def read_database(message: Message) -> None:
    """
        Выводит историю прошлых запросов пользователя в виде сообщений с изображениями.

        :param message: Объект сообщения Telegram.
    """
    with sqlite3.connect('history.db') as conn:
        cur = conn.cursor()
        cur.execute('''SELECT * FROM requests''')

        data = cur.fetchall()

        for elem in data:
            user_name = elem[1]
            time_request = elem[2]
            date_image = elem[3]
            title = elem[4]
            image_bytes = elem[5]

            photo = BytesIO(image_bytes)
            photo.name = "image.jpg"

            bot.send_message(message.chat.id,
                             f'Пользователь: {user_name}\n'
                             f'Время запроса: {time_request}\n'
                             f'Дата изображения: {date_image}\n')
            bot.send_photo(message.chat.id, photo=photo, caption=title)
