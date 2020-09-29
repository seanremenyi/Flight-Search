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
    
    @staticmethod
    def seperation():    
        print("*"*70)
            

    @classmethod
    def choose_flight(cls):
        user_input = input("\n\nWhich Flight would you like to choose?\nEnter the reference number\n")
        try: 
            int(user_input) <= len(cls.itineraries)
            os.system('clear')
            cls.seperation()
            cls.display_format(int(user_input))
            print(f"Link to Booking: {cls.itineraries[1].deep_link}")
            cls.seperation()
        except:
            cls.choose_flight()

    
    @classmethod
    def display_format(cls, num):
        print(f"""{num}   Cost: {cls.itineraries[num].price}
    From: {cls.itineraries[num].origin}    at    {cls.itineraries[num].departure_time}
    To : {cls.itineraries[num].destination}    at    {cls.itineraries[num].arrival_time}
    Extra info:
        Route: {cls.itineraries[num].routes}
        Airline Carrier : {cls.itineraries[num].airlines}
        Duration: {cls.itineraries[num].duration}
        Transfers : {cls.itineraries[num].transfer}""")
        cls.seperation()

        