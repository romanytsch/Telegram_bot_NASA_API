# Telegram-бот "Астрономическая картина дня" (NASA APOD)

## Описание

Этот Telegram-бот позволяет просматривать астрономическую картину дня с сайта 
NASA (Astronomy Picture of the Day), а также случайные картины или картины по конкретной дате. 
Пользователь может просмотреть историю своих запросов с сохранёнными изображениями.

---

## Возможности бота

- /start — приветствие и краткая инструкция с кнопками.
- /help — вывод списка доступных команд.
- /history — просмотр истории запросов с изображениями и информацией.
- /image_day — показать астрономическую картину дня.
- /image_date — ввести дату и получить картину на эту дату.
- Случайная картина и выбор даты через интерактивные кнопки клавиатуры.

---

## Установка и запуск

1. Клонируйте репозиторий.

2. Создайте виртуальное окружение и установите зависимости:

python -m venv venv
source venv/bin/activate # Unix/macOS
venv\Scripts\activate # Windows

pip install -r requirements.txt

3. Создайте файл `.env` в корне проекта с содержимым:

BOT_TOKEN=ваш_токен_бота_telegram
API_KEY=ваш_ключ_API_NASA

4. Запустите бота:

python main.py

---

## Использование

- Запустите бота в Telegram, отправьте `/start`.
- Используйте кнопки на клавиатуре или команды для получения картин.
- Для просмотра картинки на определённую дату отправьте команду `/image_date` и следуйте 
инструкции.

---

## Структура проекта

- `api/` — функции для работы с API NASA.
- `database/` — скрипты для работы с базой SQLite.
- `handlers/` — обработчики команд и сообщений Telegram.
- `keyboards/` — Inline клавиатуры для интерактивности.
- `utils/` — вспомогательные функции (перевод, проверка даты и др).
- `loader.py` — инициализация бота и хранилища состояний.
- `main.py` — точка входа и запуск бота.

---

## Логи и отладка

Логи пишутся в файл `bot.log` с уровнем INFO и выше. Это поможет отследить ошибки и 
действия бота.

---

## Требования

- Python 3.8+
- Библиотеки в `requirements.txt`, включая:
  - `pyTelegramBotAPI`
  - `requests`
  - `python-dotenv`
  - `googletrans`
  - и др.

---

## Лицензия

Проект открыт для использования и модификации.

---

## Документация ключевых функций

| Функция                           | Описание                          | Аргументы                              | Возвращает   |
|-----------------------------------|-----------------------------------|----------------------------------------|--------------|
| get_apod_day(api_key)             | Получить APOD дня                 | api_key: str                           | dict         |
| get_apod_random(api_key)          | Получить случайный APOD           | api_key: str                           | dict         |
| get_apod_data(api_key, date)      | Получить APOD по дате             | api_key: str, date: str                | dict         |
| create_tables(db_path)            | Создать таблицы                   | db_path: str = 'history.db'            | None         |
| add_database(...)                 | Добавить запись                   | user_name: str, time: str, ...         | None         |
| send_apod_day(chat_id, user)      | Отправить APOD дня                | chat_id: int, user: User               | None         |
| send_apod_random(chat_id, user)   | Отправить случайный APOD          | chat_id: int, user: User               | None         |
| send_apod_date(message)           | Отправить APOD по дате            | message: Message                       | None         |
| read_database(message)            | Показать историю                  | message: Message                       | None         |
| is_valid_date(date_text)          | Проверка даты                     | date_text: str                         | bool         |
| translate_text_google(text, dest) | Перевод текста Google Translate   | text: str, dest: str = 'ru'            | str          |