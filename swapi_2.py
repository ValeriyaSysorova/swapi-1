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

    def get_sw_categories(self, url=''):
        response = self.get(url)
        if response is not None:
            categories = json.loads(response.text).keys()
            return categories


api_req_obj = SWRequester('https://swapi.dev')
api_req_obj.get_sw_categories('/api')