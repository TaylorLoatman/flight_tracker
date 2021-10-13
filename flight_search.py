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

    def cheap_price(self, from_location, to_location, formatted_date, from_date):

        locat_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

        header = {
            'apikey': TEQUILA_APIKEY,
            'Content-Encoding': 'gzip'
        }

        params = {
            'fly_from': from_location,
            'fly_to': to_location,
            'date_from': formatted_date,
            'date_to': from_date,
            'flight_type': 'round',
            'nights_in_dst_from': '7',
            'nights_in_dst_to': '28',
            'curr': 'USD',
            'limit': '1'
        }

        response = requests.get(url=locat_endpoint, params=params, headers=header)
        data = response.json()['data'][0]['price']
        return data



