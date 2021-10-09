#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager




data_manager = DataManager()
sheet_data = data_manager.get_destenation_data()

city_list = []

for list in sheet_data:
    for element in list:
        city_list.append(element)

flight_code = []

for city in city_list:
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    work_code = flight_search.find_code(city)
    flight_code.append([work_code])

data_manager.update_destenation_code(flight_code)



