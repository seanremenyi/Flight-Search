class Itinerary():
    itineraries = {}
    count = 0
    
    @classmethod
    def add_flight(cls, flight):
        cls.itineraries[cls.count]=flight
        cls.count +=1