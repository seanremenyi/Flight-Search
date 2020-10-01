import unittest
import requests
import json
from Flights import Flight
from Itinerary import Itinerary

class ItineraryClass(unittest.TestCase):
    def test_add_flight(self):
        response_1 = requests.get(f"https://api.skypicker.com/flights?flyFrom=MEL&to=SYD&curr=AUD&dateFrom=12/12/2020&dateTo=15/12/2020&partner=picky&v=3")
        data =  json.loads(response_1.text)
        test_response = data["data"][0]
        test_flight = Flight(test_response)
        
        test_itinerary = Itinerary()
        test_itinerary.add_flight(test_flight)
        
        self.assertTrue(test_itinerary.itineraries)