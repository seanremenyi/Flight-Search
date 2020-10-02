import requests
import json
import datetime
from IataCode import IataCode


class Query():

    # Set attributes to parameters needed for API call,
    # then use attributes for the call
    def __init__(self):
        """Initialize Query object"""
        print("Welcome to my flight search application\n")
        # Attribute obtained from IataCode class
        origin = IataCode("Enter your Origin city:")
        self.origin = origin.iata_code
        # Attribute obtained from IataCode class
        destination = IataCode("Enter your Destination city:")
        self.destination = destination.iata_code
        print("""\n\nSearch Flights among a range of dates
Dates are of the format dd/mm/yyyy\n""")
        self.starting_range = self.get_date("Look for Flights from the:")
        self.ending_range = self.get_date("Look for Flights up until:")
        self.query_results = self.api_call()

    def get_date(self, question: str) -> str:
        """get date from user"""
        user_input = input(f"{question}\n")
        try:
            day, month, year = user_input.split('/')
            datetime.datetime(int(year), int(month), int(day))
            return user_input
        except ValueError:
            print("""Sorry can you try that again
(remember format is dd/mm/yyyy)""")
            return self.get_date(question)

    def api_call(self) -> dict:
        """API call with Query's attributes"""
        try:
            response = requests.get(
                "https://api.skypicker.com/"
                f"flights?flyFrom={self.origin}",
                f"&to={self.destination}&curr=AUD&dateFrom=",
                f"{self.starting_range}",
                f"&dateTo={self.ending_range}&partner=picky&v=3")
            data = json.loads(response.text)
            return data["data"]
        except:
            print("Sorry there's no flights for that date")
