from telebot.types import Message
from keyboards.inline_start import get_inline_keyboard
from loader import bot

@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!\n"
                          f"Этот Телеграм-бот выводит ""Астрономическую картину дня"" "
                          "на сегодняшний день или на заданную дату.", reply_markup=get_inline_keyboard())

