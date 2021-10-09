import requests
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

    # FROM_LOCATION = 'ATL'
    #
    # locations_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
    #
    # date = dt.datetime.today()
    # formatted_date = date.strftime("%m/%d/%Y")
    # days = dt.timedelta(days=6 * 30)
    #
    # future = date + days
    # from_date = future.strftime("%m/%d/%Y")
    # # class FlightData:
    # #     pass
    #
    # header = {
    #     'apikey': TEQUILA_APIKEY,
    #     'Content-Encoding': 'gzip'
    # }
    #
    # params = {
    #     'fly_from': FROM_LOCATION,
    #     'fly_to': 'NYC',
    #     'date_from': formatted_date,
    #     'date_to': from_date,
    #     'flight_type': 'round',
    #     'curr': 'USD'
    # }
    #
    # response = requests.get(url=locations_endpoint, params=params, headers=header)
    # req = response.json()

