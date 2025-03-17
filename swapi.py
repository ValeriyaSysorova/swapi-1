import requests
import json
from pathlib import Path


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url=''):
        base_url_request = f'{self.base_url}/'
        if len(url) > 0:
            if url[0] == '/':
                url = url[1:]
        url_req = f'{base_url_request}{url}' if url != '' else base_url_request
        try:
            response = requests.get(url_req)
            response.raise_for_status()
            return response
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):
    def get_sw_categories(self):
        response = self.get()
        if response is not None:
            categories = json.loads(response.text).keys()
            return categories

    def get_sw_info(self, sw_type):
        response_cat = self.get(f'{sw_type}/')
        return response_cat.text


def save_sw_data(base_url='https://swapi.dev/api'):
    # Создали объект класса.
    api_req_obj = SWRequester(base_url)
    # Создали папку data.
    Path('data').mkdir(exist_ok=True)
    # Получили список категорий.
    categories = api_req_obj.get_sw_categories()
    for category in categories:
        info = api_req_obj.get_sw_info(category)
        with open(f"data/{category}.txt", 'w', encoding='utf-8') as f:
            f.write(info)