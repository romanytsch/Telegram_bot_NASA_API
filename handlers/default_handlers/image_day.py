import requests
from telebot.types import Message, User
from api.apod_api import get_apod_day, get_apod_random
from config_data.config import API_KEY
from loader import bot
from utils.translate import translate_text_google
from keyboards.inline_random import get_inline_keyboard_random
from database.queries import add_database
import datetime


def send_apod_day(chat_id: int, user: User) -> None:
    """
        Осуществляет отправку астрономической картины дня пользователю Telegram и записывает запрос в базу.

        :param chat_id: Идентификатор чата для отправки сообщения.
        :param user: Объект пользователя Telegram (User).
    """
    data = get_apod_day(API_KEY)
    if data.get("media_type") == "image":
        date = data.get("date", "")
        image_url = data.get("url", "")

        response = requests.get(image_url)
        if response.status_code == 200:
            image_bytes = response.content
        else:
            image_bytes = None

        explanation = data.get("explanation", "")
        explanation_translated = translate_text_google(explanation)
        title = data.get("title", "")
        title_translated = translate_text_google(title)

        time_now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        add_database(user.full_name, time_now, date, title_translated, image_bytes)

        caption = f"<b>{date}</b>\n\n<b>{title_translated}</b>\n\n{explanation_translated}"
        MAX_CAPTION_LENGTH = 1024

        if len(caption) > MAX_CAPTION_LENGTH:
            # Отправляем только заголовок в caption, а описание отдельным сообщением
            bot.send_photo(chat_id,
                           image_url,
                           caption=f"<b>{date}</b>\n\n<b>{title_translated}</b>",
                           parse_mode='HTML')
            bot.send_message(chat_id,
                             explanation_translated,
                             reply_markup=get_inline_keyboard_random())
        else:
            bot.send_photo(chat_id,
                           image_url,
                           caption=caption,
                           parse_mode='HTML',
                           reply_markup=get_inline_keyboard_random())
    else:
        url = data.get('url') or data.get('hdurl') or "Изображение недоступно"
        bot.send_message(chat_id, f"{data['title']}\n{url}")



def send_apod_random(chat_id: int, user: User) -> None:
    """
        Осуществляет отправку случайной астрономической картины дня пользователю Telegram и записывает запрос в базу.

        :param chat_id: Идентификатор чата для отправки сообщения.
        :param user: Объект пользователя Telegram (User).
    """
    data = get_apod_random(API_KEY)
    if data.get("media_type") == "image":
        date = data.get("date", "")
        image_url = data.get("url", "")

        response = requests.get(image_url)
        if response.status_code == 200:
            image_bytes = response.content
        else:
            image_bytes = None

        explanation = data.get("explanation", "")
        explanation_translated = translate_text_google(explanation)
        title = data.get("title", "")
        title_translated = translate_text_google(title)

        time_now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        add_database(user.full_name, time_now, date, title_translated, image_bytes)

        caption = f"<b>{date}</b>\n\n<b>{title_translated}</b>\n\n{explanation_translated}"
        MAX_CAPTION_LENGTH = 1024

        if len(caption) > MAX_CAPTION_LENGTH:
            # Отправляем только заголовок в caption, а описание отдельным сообщением
            bot.send_photo(chat_id,
                           data["url"],
                           caption=f"<b>{date}</b>\n\n<b>{title_translated}</b>",
                           parse_mode='HTML')
            bot.send_message(chat_id,
                             explanation_translated,
                             reply_markup=get_inline_keyboard_random())
        else:
            bot.send_photo(chat_id,
                           data["url"],
                           caption=caption,
                           parse_mode='HTML',
                           reply_markup=get_inline_keyboard_random())
    else:
        url = data.get('url') or data.get('hdurl') or "Изображение недоступно"
        bot.send_message(chat_id, f"{data['title']}\n{url}")


@bot.message_handler(commands=['image_day'])
def send_apod(message: Message):
    send_apod_day(message.chat.id, message.from_user)
