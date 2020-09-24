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



# print(data["data"][0])

flight1=Flight(data["data"][0])
flight1.get_origin()
flight1.get_destination()
flight1.get_price()
flight1.get_departure_time_UTC()
flight1.get_departure_time()
flight1.get_arrival_time_UTC()
flight1.get_arrival_time()
flight1.get_deep_link()
flight1.get_duration()
flight1.get_airlines()
flight1.get_routes()
# print(flight1.origin)
# print(flight1.destination)
# print(flight1.price)
# # print(flight1.departure_time_UTC)
# print(flight1.departure_time)
# # print(flight1.arrival_time_UTC)
# print(flight1.arrival_time)
# # print(flight1.deep_link)
# print(flight1.duration)
# print(flight1.airlines)
# print(flight1.routes)

Itinerary.add_flight(flight1)
print(Itinerary.itineraries[0].origin)

# for items in data["data"]:
#     print(f'From {items["cityFrom"]}, {items["countryFrom"]["name"]} to {items["cityTo"]}, {items["countryTo"]["name"]} for {items["price"]}')


