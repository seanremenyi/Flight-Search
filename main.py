from Query import Query
from Flights import Flight
from Itinerary import Itinerary

new_query = Query()

for flights in new_query.query_results:
    Itinerary.add_flight(Flight(flights))

Itinerary.list_results()

user_input = input("\n\nWhich Flight would you like? enter reference num\n\n")

Itinerary.choice(int(user_input))



# import requests
# import json

# response = requests.get(f"https://api.skypicker.com/flights?flyFrom=MEL&to=SYD&curr=AUD&dateFrom=05/10/2020&dateTo=10/10/2020&partner=picky&v=3")
# data = json.loads(response.text)
# print(data["data"])