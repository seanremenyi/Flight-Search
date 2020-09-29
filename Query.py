import requests
import json
import datetime
from IataCode import IataCode

class Query():
    
    def __init__(self):
        print("Country Codes must be the IATA code for the Airport\nIATA codes are the corresponding 3 Capitalized letters\n")
        origin= IataCode("Enter your Origin city:")
        self.origin = origin.iata_code
        destination = IataCode("Enter your Destinatin city:")
        self.destination = destination.iata_code
        print("\n\nSearch Flights among a range of dates\nDates are of the format dd/mm/yyyy\n")
        self.starting_range = self.get_date("Look for Flights from the:")
        self.ending_range = self.get_date("Look for Flights up until:")
        self.query_results = self.api_call()


    def get_date(self, question):
        user_input = input(f"{question}\n")
        try :
            day,month,year = user_input.split('/')
            datetime.datetime(int(year),int(month),int(day))
            return user_input
        except ValueError:
            self.get_date(question)

    
    def api_call(self):
        response = requests.get(f"https://api.skypicker.com/flights?flyFrom={self.origin}&to={self.destination}&curr=AUD&dateFrom={self.starting_range}&dateTo={self.ending_range}&partner=picky&v=3")
        data =  json.loads(response.text)
        return data["data"]    
        