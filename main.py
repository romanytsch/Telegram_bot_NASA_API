from loader import bot
from utils.set_default_commands import set_default_commands
from handlers.default_handlers.message_handler import handle_text

if __name__ == "__main__":
    set_default_commands(bot)
    bot.message_handler(func=lambda message: True)(handle_text)
    bot.infinity_polling()
