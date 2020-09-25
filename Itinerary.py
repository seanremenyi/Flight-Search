import os

class Itinerary():
    itineraries = {}
    count = 1
    
    @classmethod
    def add_flight(cls, flight):
        cls.itineraries[cls.count]=flight
        cls.count +=1
    
    @classmethod
    def list_results(cls):
        for items in cls.itineraries:
            cls.display_format(items)

    @classmethod
    def choice(cls):
        user_input = input("Which Flight would you like to choose?\nEnter the reference number")
        try: 
            int(user_input) <= len(cls.itineraries)
            os.system('clear')
            print("*******************************************************************************)
            cls.display_format(user_input)
            print(f"Link to Booking: {cls.itineraries[int].deep_link}")
            

    
    @classmethod
    def display_format(cls, num):
            print(f"""{num}   Cost: {cls.itineraries[num].price}
    From: {cls.itineraries[num].origin}    at    {cls.itineraries[num].departure_time}
    To : {cls.itineraries[num].destination}    at    {cls.itineraries[num].arrival_time}
    Extra info:
        Route: {cls.itineraries[num].routes}
        Airline Carrier : {cls.itineraries[num].airlines}
        Duration: {cls.itineraries[num].duration}
        Transfers : {cls.itineraries[num].transfer}
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
        
        