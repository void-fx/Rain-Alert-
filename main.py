# import os
from twilio.rest import Client
import requests

ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "5cf2cba26e859c52c311279f12dd76b0"
account_sid = "ACfa57a75e7d9739450f3f891d8c0fe05b"
auth_token = "7cc7a38abc55e1c1b3d38bd1746c6502"

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
    
