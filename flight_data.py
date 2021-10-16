import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_APIKEY = os.environ.get('TEQUILA_ENDPOINT')

class Flight_data:

    def cheap_price(self, from_location, to_location, formatted_date, from_date):

        locate_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

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

        response = requests.get(url=locate_endpoint, params=params, headers=header)
        data = response.json()['data'][0]['price']
        return data






