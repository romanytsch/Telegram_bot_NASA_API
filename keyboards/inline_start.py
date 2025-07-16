from typing import Any

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard() -> Any:
    """
        Возвращает инлайн-клавиатуру для стартового меню.

        :return: Объект клавиатуры `InlineKeyboardMarkup`.
    """
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("Картина дня", callback_data="btn_image_day")
    button2 = InlineKeyboardButton("Картина по дате", callback_data="btn_image_data")
    keyboard.add(button1, button2)
    return keyboard