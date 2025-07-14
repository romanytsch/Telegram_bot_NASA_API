import logging

logging.basicConfig(
    level=logging.INFO,  # уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot.log',  # лог будет писаться в файл bot.log
    filemode='a',  # режим добавления в файл (a - append)
    encoding='utf-8'     # кодировка файла
)

