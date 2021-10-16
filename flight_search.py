import requests
from pprint import pprint
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_APIKEY = os.environ.get('TEQUILA_ENDPOINT')



class FlightSearch:

    def find_code(self, city_name):
        header = {
            'accept': 'application/json',
            'apikey': TEQUILA_APIKEY
            }

        data_params = {
            'term': city_name,
            'location_types': 'city',
        }

        locations_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        response = requests.get(url=locations_endpoint, params=data_params, headers=header)
        results = response.json()['locations'][0]['code']
        return results





