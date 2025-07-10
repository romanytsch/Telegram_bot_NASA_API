import os
from dotenv import find_dotenv, load_dotenv

# Загружаем переменные окружения из файла .env
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("hello_world", "Приветствие")
)