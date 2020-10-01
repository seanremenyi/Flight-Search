import unittest
import requests
import json
from Flights import Flight

class TestFlightClass(unittest.TestCase):
    def test_init(self):
        response = requests.get(f"https://api.skypicker.com/flights?flyFrom=MEL&to=SYD&curr=AUD&dateFrom=12/12/2020&dateTo=15/12/2020&partner=picky&v=3")
        data =  json.loads(response.text)
        test_response = data["data"][0]
        test_flight = Flight(test_response)

        self.assertEqual(test_flight.origin,"Melbourne, Australia")
        self.assertEqual(test_flight.destination,"Sydney, Australia")
        
        self.assertTrue(test_flight.price)
        self.assertTrue(test_flight.departure_time_UTC)
        self.assertTrue(test_flight.departure_time)
        self.assertTrue(test_flight.arrival_time_UTC)
        self.assertTrue(test_flight.arrival_time)
        self.assertTrue(test_flight.deep_link)
        self.assertTrue(test_flight.duration)
        self.assertTrue(test_flight.airlines)
        
        

        