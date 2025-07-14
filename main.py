from loader import bot
from utils.set_default_commands import set_default_commands
from handlers.default_handlers.message_handler import handle_text
import logging
from database.connections import create_tables

if __name__ == "__main__":
    create_tables()
    logging.info("Запуск бота")
    set_default_commands(bot)
    logging.info("Команды бота установлены")


    bot.message_handler(func=lambda message: True)(handle_text)
    logging.info("Обработчик сообщений зарегистрирован")

    try:
        bot.infinity_polling()
    except Exception as e:
        logging.error(f"Ошибка при работе бота: {e}", exc_info=True)
