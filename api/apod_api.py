import requests
import json

def get_apod_day(api_key):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    response = json.loads(raw_response.text)
    return response

def get_apod_random(api_key):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count=1')
    response = json.loads(raw_response.text)
    return response[0]

def get_apod_data(api_key, date):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}')
    response = json.loads(raw_response.text)
    return response
