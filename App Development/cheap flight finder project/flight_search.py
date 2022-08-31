import requests
from flight_data import FlightData
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
HEADERS = {
            "apikey": "E6tDOKiRNqdYHVojlGjGJO9r1druwcNY"
        }

SEARCHING_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
SHEETY_ENDPOINT_PUT = "https://api.sheety.co/3f53816e11ac16d583f262f3ff2428cf/flightDealsLatha/prices"

class FlightSearch:
    def get_destination_code(self, city_name):
        parameters_kiwi = {
            "term": city_name
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=parameters_kiwi , headers=HEADERS)
        list_locations = response.json()["locations"]
        code = list_locations[0]["code"]
        return code

    def search_flight(self, origin_city, destination_city, from_time, to_time):
        parameters_flight_search = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=SEARCHING_FLIGHT_ENDPOINT, params=parameters_flight_search, headers=HEADERS)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
