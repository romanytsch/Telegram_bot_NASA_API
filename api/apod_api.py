import requests
import json
from typing import Optional, Any, Dict


def get_apod_day(api_key: str) -> Dict[str, Any]:
    """
        Получить данные астрономической картины дня (APOD) с помощью API NASA.

        :param api_key: API ключ NASA.
        :return: Данные APOD в формате словаря.
    """
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    response = json.loads(raw_response.text)
    return response

def get_apod_random(api_key: str) -> Dict[str, Any]:
    """
        Получить данные случайной астрономической картины дня (APOD) с помощью API NASA.

        :param api_key: API ключ NASA.
        :return: Данные случайной APOD в формате словаря.
    """
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count=1')
    response = json.loads(raw_response.text)
    return response[0]

def get_apod_data(api_key: str, date: str) -> Dict[str, Any]:
    """
        Получить данные APOD за конкретную дату.

        :param api_key: API ключ NASA.
        :param date: Дата в формате 'YYYY-MM-DD'.
        :return: Данные APOD в формате словаря.
    """
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}')
    response = json.loads(raw_response.text)
    return response
