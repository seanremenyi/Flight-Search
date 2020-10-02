import sys
from Query import Query
from Flights import Flight
from Itinerary import Itinerary

# Create Query object
new_query = Query()

# Iterate through every flight in API respons
try:
    for flights in new_query.query_results:
        # Create flight objects and add to Itinerary object
        Itinerary.add_flight(Flight(flights))
except:
    # exit program if no flights found
    sys.exit(0)

# Print all flight objects to terminal
Itinerary.list_results()

# User chooses a flight
Itinerary.choose_flight()
