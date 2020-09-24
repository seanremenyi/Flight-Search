import os

class Itinerary():
    itineraries = {}
    count = 1
    
    @classmethod
    def add_flight(cls, flight):
        cls.itineraries[cls.count]=flight
        cls.count +=1
    
    @classmethod
    def price_sort(cls):
        for items in cls.itineraries:
            print(f"""{items}   Cost: {cls.itineraries[items].price}
    From: {cls.itineraries[items].origin}    at    {cls.itineraries[items].departure_time}
    To : {cls.itineraries[items].destination}    at    {cls.itineraries[items].arrival_time}
    Extra info:
        Route: {cls.itineraries[items].routes}
        Airline Carrier : {cls.itineraries[items].airlines}
        Duration: {cls.itineraries[items].duration}
        Transfers : {cls.itineraries[items].transfer}
*******************************************************************************""")

    @classmethod
    def choice(cls, int):
        os.system('clear')
        print(f"""*******************************************************************************
{int}   Cost: {cls.itineraries[int].price}
    From: {cls.itineraries[int].origin}    at    {cls.itineraries[int].departure_time}
    To : {cls.itineraries[int].destination}    at    {cls.itineraries[int].arrival_time}
    Extra info:
        Route: {cls.itineraries[int].routes}
        Airline Carrier : {cls.itineraries[int].airlines}
        Duration: {cls.itineraries[int].duration}
        Transfers : {cls.itineraries[int].transfer}
        
Link to Booking: {cls.itineraries[int].deep_link}        
*******************************************************************************""")
        
        