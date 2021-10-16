from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import Flight_data
from notification_manager import NotificationManager
import datetime as dt

# Constants
FROM_LOCATION = 'ATL'

# Classes
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = Flight_data()
send_Message = NotificationManager()

# Data Containers
city_list = []
flight_code = []
price_list = []
new_low_list = []
formatted_updated_list = []

# Getting city data from Google Sheets to find IATA Code
sheet_data = data_manager.get_dest_data()

for city in sheet_data:
    if city == 'City':
        pass
    else:
        city_list.append(city)

for city in city_list:
    work_code = flight_search.find_code(city)
    flight_code.append([work_code])

# Update Google Sheet with IATA code
data_manager.update_dest_code(flight_code)

# Date Variables
date = dt.datetime.today() - dt.timedelta(days=1)
formatted_date = date.strftime("%d/%m/%Y")
days = dt.timedelta(days=6 * 30)

future = date + days
from_date = future.strftime("%d/%m/%Y")

# Price Data
for i in flight_code:
    to_location = i
    prices = flight_data.cheap_price(FROM_LOCATION, to_location, formatted_date, from_date)
    price_list.append(prices)

lowest_list = data_manager.get_lowest_price_data()

# Correct Price format for Google Sheets
for p in lowest_list:
    if p == 'Lowest Price':
        pass
    else:
        new_low_list.append(int(p))

# Update Lowest Price Data and notifies user of price drop
for i, j in zip(price_list, new_low_list):
    if j > i:
        formatted_updated_list.append([f'{j}'])
        send_Message.send_alert()
    else:
        formatted_updated_list.append([f'{i}'])


data_manager.fill_low(formatted_updated_list)

