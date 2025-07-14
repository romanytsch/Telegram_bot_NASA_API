from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton("Картина дня", callback_data="btn_image_day")
    button2 = InlineKeyboardButton("Картина по дате", callback_data="btn_image_data")
    keyboard.add(button1, button2)
    return keyboard