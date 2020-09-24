import requests
import json
import datetime, pytz


class Flights():
    def __init__(self, flight_data):
        self.flight_data = flight_data
        
    def get_origin(self):
        self.origin = f'{self.flight_data["cityFrom"]}, {self.flight_data["countryFrom"]["name"]}' 
    
    def get_destination(self):
        self.destination = f'{self.flight_data["cityTo"]}, {self.flight_data["countryTo"]["name"]}' 

    def get_price(self):
        self.price = self.flight_data["price"]
        
    @staticmethod
    def convert_timestamp(timestamp):
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        conv_timestamp=timestamp.astimezone(pytz.timezone("Australia/Melbourne"))
        return conv_timestamp.strftime('%d/%m/%y %H:%M:%S')
        
    def get_departure_time(self):
        self.departure_time = self.convert_timestamp(self.flight_data['dTimeUTC'])

    def get_arrival_time(self):
        self.arrival_time = self.convert_timestamp(self.flight_data['aTimeUTC'])    

    def get_deep_link(self):
        self.deep_link= self.flight_data["deep_link"]
    
    def get_duration(self):
        self.duration = self.flight_data["duration"]
        
    def get_transfers(self):
        if self.flight_data["transfer"] == []:
            self.transfer = "No transfer"
        else:
            self.transfer = self.flight_data["transfer"]
            
    def get_routes(self):
        self.routes = self.flight_data["routes"]

    def get_airlines(self):
        self.airlines = self.flight_data["airlines"]
    


# origin = input("Where are you flying from?\n")
# destination= input("Where would you like to go\n")
# strarting_range= input("Looking at flights from the date?\n")
# ending_range= input("To the date\n")

# response = requests.get(f"https://api.skypicker.com/flights?flyFrom={origin}&to={destination}&curr=AUD&dateFrom={strarting_range}&dateTo={ending_range}&partner=picky&v=3")

response = requests.get(f"https://api.skypicker.com/flights?flyFrom=MEL&to=SYD&curr=AUD&dateFrom=05/10/2020&dateTo=10/10/2020&partner=picky&v=3")

data = json.loads(response.text)

print(data["data"][0])

# flight1=Flights(data["data"][0])
# flight1.get_departure_time()
# print(flight1.departure_time)

# for items in data["data"]:
#     print(f'From {items["cityFrom"]}, {items["countryFrom"]["name"]} to {items["cityTo"]}, {items["countryTo"]["name"]} for {items["price"]}')


