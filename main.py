#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt

FROM_LOCATION = 'ATL'

data_manager = DataManager()
sheet_data = data_manager.get_destenation_data()

flight_search = FlightSearch()

city_list = []

for list in sheet_data:
    for element in list:
        city_list.append(element)

flight_code = []

for city in city_list:
    work_code = flight_search.find_code(city)
    flight_code.append([work_code])

data_manager.update_destenation_code(flight_code)

date = dt.datetime.today() - dt.timedelta(days=1)
formatted_date = date.strftime("%d/%m/%Y")
days = dt.timedelta(days=6 * 30)

future = date + days
from_date = future.strftime("%d/%m/%Y")

price_list = []

for i in flight_code:
    to_location = i
    prices = flight_search.cheap_price(FROM_LOCATION, to_location, formatted_date, from_date)
    price_list.append(prices)

lowest_list = data_manager.get_lowest_price_data()
new_low_list = []

for p in lowest_list:
    new_low_list.append(p[0])




# low_price_dict = {}
for i,j in zip(city_list, new_low_list):
    print(f"{i}: ${j}\n")




