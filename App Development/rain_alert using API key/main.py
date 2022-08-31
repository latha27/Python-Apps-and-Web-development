import requests
from twilio.rest import Client

account_sid = "ACb55e64befd991304125b5fb64fa46175"
account_auth_token = "6d5eaf0f2df5cdf443288f1d8b25344a"

parameters = {
    "lat": 61.006550,
    "lon": 14.537510,
    "appid": "93a1cfa4dc030b1a1fe429e75b3ef588",
    "exclude": "current,minutely,daily",

}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
hourly_data = response.json()["hourly"]
# for id_num in range(len(hourly_data)):
twelve_hour_data = hourly_data[0:13]

will_rain = False
for weather in twelve_hour_data:
    id_num = weather["weather"][0]["id"]
    if id_num < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, account_auth_token)
    message = client.messages \
        .create(body="It's going to be rain today. Remember to bring an ☂",
                from_="+19805258168", to="+32467606413",
    )
    print(message.status)

