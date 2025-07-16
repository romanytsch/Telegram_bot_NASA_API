import requests
from telebot.types import Message

from config_data.config import API_KEY
from database.queries import add_database
from keyboards.inline_random import get_inline_keyboard_random
from loader import bot
from utils.translate import translate_text_google
from utils.valid_date import is_valid_date
from api.apod_api import get_apod_data
import datetime



@bot.message_handler(commands=["image_date"])
def ask_for_date(message: Message) -> None:
    bot.send_message(message.chat.id, "Введите дату в формате ГГГГ-ММ-ДД (например, 2023-07-14), но не ранее 16 июня 1995:")


@bot.message_handler(func=lambda msg: is_valid_date(msg.text))
def send_apod_date(message: Message) -> None:
    """
        Отправляет картину дня по введённой пользователем дате и записывает запрос в базу.

        :param message: Объект сообщения Telegram, содержащий дату.
    """
    date = message.text.strip()
    if not is_valid_date(date):
        msg = bot.send_message(message.chat.id,
                               "Неверный формат даты или дата вне допустимого диапазона. Попробуйте ещё раз:")
        bot.register_next_step_handler(msg, send_apod_date)
        return
    data = get_apod_data(API_KEY, date)
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
        add_database(message.from_user.full_name, time_now, date, title_translated, image_bytes)

        caption = f"<b>{date}</b>\n\n<b>{title_translated}</b>\n\n{explanation_translated}"
        MAX_CAPTION_LENGTH = 1024

        if len(caption) > MAX_CAPTION_LENGTH:
            bot.send_photo(message.chat.id,
                           data["url"],
                           caption=f"<b>{date}</b>\n\n<b>{title_translated}</b>",
                           parse_mode='HTML')
            bot.send_message(message.chat.id,
                             explanation_translated,
                             reply_markup=get_inline_keyboard_random())
        else:
            bot.send_photo(message.chat.id,
                           data["url"],
                           caption=caption,
                           parse_mode='HTML',
                           reply_markup=get_inline_keyboard_random())
    else:
        bot.send_message(message.chat.id, f"{data['title']}\n{data['url']}")