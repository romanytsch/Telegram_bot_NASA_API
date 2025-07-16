from telebot.types import Message

from loader import bot


def handle_text(message: Message) -> None:
    """
        Обрабатывает произвольные текстовые сообщения, не являющиеся командами.

        :param message: Объект сообщения Telegram.
    """
    user_text = message.text

    if user_text == 'Привет':
        bot.send_message(message.chat.id, "Как дела?")