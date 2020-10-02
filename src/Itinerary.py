import os
from Flights import Flight


class Itinerary():
    # Class attributes for all Flight objects from AIP response
    itineraries = {}
    count = 1

    @classmethod
    def add_flight(cls, flight: Flight) -> None:
        """Add flights to itinerary class atribute"""
        cls.itineraries[cls.count] = flight
        cls.count += 1

    @classmethod
    def list_results(cls) -> None:
        """Display all Flights from original Query"""
        for items in cls.itineraries:
            cls.display_format(items)

    @staticmethod
    def seperation() -> None:
        """Formating purposes"""
        print("*"*70)

    @classmethod
    def choose_flight(cls) -> None:
        """Gives user the link for the flight they choose"""
        user_input = input("""\n\nWhich Flight would you like to choose?
Enter the reference number\n""")
        try:
            int(user_input) <= len(cls.itineraries)
            os.system('clear')
            cls.seperation()
            cls.display_format(int(user_input))
            print(f"Link to Booking: {cls.itineraries[1].deep_link}")
            cls.seperation()
            print("\nAlways check the details, they can change on a dime\n")
            cls.seperation()
        except:
            cls.choose_flight()

    @classmethod
    def display_format(cls, num: int) -> None:
        """display Flight information"""
        origin = cls.itineraries[num].origin
        departure_time = cls.itineraries[num].departure_time
        destination = cls.itineraries[num].destination
        arrival_time = cls.itineraries[num].arrival_time
        price = cls.itineraries[num].price
        airlines = cls.itineraries[num].airlines
        duration = cls.itineraries[num].duration
        print(f"""{num}   Cost: {price}
    From: {origin}    at    {departure_time}
    To : {destination}    at    {arrival_time}
    Extra info:
        Airline Carrier : {airlines}
        Duration: {duration}""")
        cls.seperation()
