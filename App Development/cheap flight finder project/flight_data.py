import requests
from pprint import pprint


SEARCHING_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
SHEETY_ENDPOINT_PUT = "https://api.sheety.co/3f53816e11ac16d583f262f3ff2428cf/flightDealsLatha/prices"


HEADERS = {
            "apikey": "E6tDOKiRNqdYHVojlGjGJO9r1druwcNY"
        }
#This class is responsible for structuring the flight data.


class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date








