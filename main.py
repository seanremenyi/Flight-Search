import requests
import json

response = requests.get("https://api.skypicker.com/flights?flyFrom=PRG&to=LGW&curr=AUD&dateFrom=18/11/2020&dateTo=12/12/2020&partner=picky&v=3")

data = json.loads(response.text)

print(data)