from telebot.types import Message
from api.apod_api import get_apod_day, get_apod_random
from config_data.config import API_KEY
from loader import bot
from utils.translate import translate_text_google
from keyboards.inline_random import get_inline_keyboard_random



def send_apod_day(chat_id):
    data = get_apod_day(API_KEY)
    if data.get("media_type") == "image":
        date = data.get("date", "")
        explanation = data.get("explanation", "")
        explanation_translated = translate_text_google(explanation)
        title = data.get("title", "")
        title_translated = translate_text_google(title)

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
        bot.send_message(chat_id, f"{data['title']}\n{data['url']}")



def send_apod_random(chat_id):
    data = get_apod_random(API_KEY)
    if data.get("media_type") == "image":
        date = data.get("date", "")
        explanation = data.get("explanation", "")
        explanation_translated = translate_text_google(explanation)
        title = data.get("title", "")
        title_translated = translate_text_google(title)

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
        bot.send_message(chat_id, f"{data['title']}\n{data['url']}")


@bot.message_handler(commands=['image_day'])
def send_apod(message: Message):
    send_apod_day(message.chat.id)
