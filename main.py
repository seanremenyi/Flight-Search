import requests
import json
from Flights import Flight
from Itinerary import Itinerary



# origin = input("Where are you flying from?\n")
# destination= input("Where would you like to go\n")
# strarting_range= input("Looking at flights from the date?\n")
# ending_range= input("To the date\n")

# response = requests.get(f"https://api.skypicker.com/flights?flyFrom={origin}&to={destination}&curr=AUD&dateFrom={strarting_range}&dateTo={ending_range}&partner=picky&v=3")

response = requests.get(f"https://api.skypicker.com/flights?flyFrom=MEL&to=SYD&curr=AUD&dateFrom=05/10/2020&dateTo=10/10/2020&partner=picky&v=3")

data = json.loads(response.text)

# g=[enumerate(Flight(flights)) for flights in data["data"]]
# print(g)
    

for flights in data["data"]:
    Itinerary.add_flight(Flight(flights))


print(Itinerary.itineraries)

# for items in data["data"]:
#     print(f'From {items["cityFrom"]}, {items["countryFrom"]["name"]} to {items["cityTo"]}, {items["countryTo"]["name"]} for {items["price"]}')


