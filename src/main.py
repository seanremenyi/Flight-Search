from Query import Query
from Flights import Flight
from Itinerary import Itinerary

new_query = Query()

for flights in new_query.query_results:
    Itinerary.add_flight(Flight(flights))

Itinerary.list_results()

Itinerary.choose_flight()
