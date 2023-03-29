# import os
from twilio.rest import Client
import requests

ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
# create a twilio account to obtain the credentials below
API_KEY = "**************************"
account_sid = "***************************"
auth_token = "*********************************"

PARAMS = {
    "lat": -4.441931,
    "lon": 15.266293,
    "appid": API_KEY,
    "exclude": "minutely,daily,current",
}

response = requests.get(url=ENDPOINT, params=PARAMS)
response.raise_for_status()
data = response.json()["hourly"][:12]

will_rain = False
for i in data:
    if i["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Bring an Umbrella",
                        from_="+18647131194",
                        to="+916380539588",
                    )
    print(message.sid)
    
