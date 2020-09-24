class Itinerary():
    itineraries = []
    
    @classmethod
    def add_flight(cls, flight):
        cls.itineraries.append(Flight)