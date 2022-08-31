import requests
from pprint import pprint
SHEETY_ENDPOINT_PUT = "https://api.sheety.co/1d7f7fcf45a045ed699bb5e658c743de/flightDealsLatha/prices"
SHEETY_ENDPOINT_POST = "https://api.sheety.co/1d7f7fcf45a045ed699bb5e658c743de/flightDealsLatha/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT_PUT)
        data = response.json()
        self.destination_data = data["price"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT_PUT}/{city['id']}", json=new_data)
            return response.text

    def update_user_data(self, first_name, last_name, email):
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
           }
        }
        response = requests.post(url=SHEETY_ENDPOINT_POST, json=new_data)
        return response.text







