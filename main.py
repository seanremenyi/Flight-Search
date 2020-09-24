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

    
# origin = input("Where are you flying from?\n")
# destination= input("Where would you like to go\n")
# strarting_range= input("Looking at flights from the date?\n")
# ending_range= input("To the date\n")

# response = requests.get(f"https://api.skypicker.com/flights?flyFrom={origin}&to={destination}&curr=AUD&dateFrom={strarting_range}&dateTo={ending_range}&partner=picky&v=3")

response = requests.get(f"https://api.skypicker.com/flights?flyFrom=MEL&to=SYD&curr=AUD&dateFrom=05/10/2020&dateTo=10/10/2020&partner=picky&v=3")

data = json.loads(response.text)

flight1=Flights(data["data"][0])
flight1.get_origin()
print(flight1.origin)

# for items in data["data"]:
#     print(f'From {items["cityFrom"]}, {items["countryFrom"]["name"]} to {items["cityTo"]}, {items["countryTo"]["name"]} for {items["price"]}')

# def get_sunset(num):
#     timestamp = datetime.datetime.fromtimestamp(num)
#     conv_timestamp=timestamp.astimezone(pytz.timezone("Australia/Melbourne"))
#     return conv_timestamp.strftime('%d/%m/%y %H:%M:%S')


# print(get_sunset(data['data'][0]['dTimeUTC']))

# print(data['data'][0]["fly_duration"])
# print(data['data'][0]["cityFrom"])
# print(data['data'][0]["countryFrom"]["name"])
# print(data['data'][0]["cityTo"])
# print(data['data'][0]["countryTo"]["name"])
# print(data['data'][0]["price"])
