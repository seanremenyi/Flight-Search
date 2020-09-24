import datetime, pytz

class Flight():
    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.get_origin()
        self.get_destination()
        self.get_price()
        self.get_departure_time_UTC()
        self.get_departure_time()
        self.get_arrival_time_UTC()
        self.get_arrival_time()
        self.get_deep_link()
        self.get_duration()
        self.get_transfers()
        self.get_routes()
        self.get_airlines()
        
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
        
    def get_departure_time_UTC(self):
        self.departure_time_UTC= self.flight_data['dTimeUTC']
        
    def get_departure_time(self):
        self.departure_time = self.convert_timestamp(self.flight_data['dTimeUTC'])

    def get_arrival_time_UTC(self):
        self.arrival_time_UTC= self.flight_data['aTimeUTC']
        
    def get_arrival_time(self):
        self.arrival_time = self.convert_timestamp(self.flight_data['aTimeUTC'])    

    def get_deep_link(self):
        self.deep_link= self.flight_data["deep_link"]
    
    def get_duration(self):
        self.duration = self.flight_data["fly_duration"]
        
    def get_transfers(self):
        if self.flight_data["transfers"] == []:
            self.transfer = "No transfer"
        else:
            self.transfer = self.flight_data["transfers"]
            
    def get_routes(self):
        self.routes = self.flight_data["routes"]

    def get_airlines(self):
        self.airlines = self.flight_data["airlines"]