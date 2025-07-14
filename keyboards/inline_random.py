from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard_random():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("Случайная картина дня", callback_data="btn_image_random")
    button2 = InlineKeyboardButton("Картина по дате", callback_data="btn_image_data")
    keyboard.add(button1, button2)
    return keyboard