from telebot.types import Message

from loader import bot


def handle_text(message: Message):
    user_text = message.text

    if user_text == 'Привет':
        bot.send_message(message.chat.id, "Как дела?")