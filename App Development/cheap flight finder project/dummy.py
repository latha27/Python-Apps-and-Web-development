import requests

SHEETY_ENDPOINT_POST = "https://api.sheety.co/1d7f7fcf45a045ed699bb5e658c743de/flightDealsLatha/users"
SHEETY_ENDPOINT_PUT = "https://api.sheety.co/1d7f7fcf45a045ed699bb5e658c743de/flightDealsLatha/prices"
def update_user_data():
    # new_data = {
    #    "user": {
    #        "iataCode": city["iataCode"]
    #   }
    # }
    response = requests.get(url=SHEETY_ENDPOINT_POST)
    print(response.json())
update_user_data()


def get_destination_data():
    response = requests.get(url=SHEETY_ENDPOINT_PUT)
    data = response.json()
    print(data)
get_destination_data()