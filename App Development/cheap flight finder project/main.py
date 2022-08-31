#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager


ORIGIN_CITY = "LON"

TODAY = datetime.now().strftime("%d/%m/%Y")
SIX_MONTH_FROM_TODAY = (datetime.now() + relativedelta(months=6)).strftime("%d/%m/%Y")

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
response = requests.get(url="https://api.sheety.co/1d7f7fcf45a045ed699bb5e658c743de/flightDealsLatha/prices")

result = response.json()
sheet_data = result["prices"]
for row in sheet_data:
    if row["iataCode"] == '':
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_data()

for destination in sheet_data:
    flight = flight_search.search_flight(ORIGIN_CITY, destination["iataCode"],from_time=TODAY, to_time=SIX_MONTH_FROM_TODAY)

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")

print("Welcome to Latha's Flight Club \n We find the best deals and email you.")
first_name_input = input("What is your first name?")
last_name_input = input("What is your last name?")
email_id_input = input("What is your email?")
confirmation_email = input("Type the email again.")

is_email = True
while is_email:
    if email_id_input != confirmation_email:
        print("Enter the correct email id")
        confirmation_email = input("Type the email again.")
    else:
        data_manager.update_user_data(first_name_input, last_name_input, email_id_input)
        print("You're in the club!")
        is_email = False
















