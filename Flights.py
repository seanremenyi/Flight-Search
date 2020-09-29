import datetime, pytz

class Flight():
    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.origin = f'{self.strip_info("cityFrom")}, {self.strip_info("countryFrom")["name"]}'
        self.destination =f'{self.strip_info("cityTo")}, {self.strip_info("countryTo")["name"]}'
        self.price= self.convert_to_price(self.strip_info("price"))
        self.departure_time_UTC = self.strip_info("dTimeUTC")
        self.departure_time = self.convert_timestamp(self.departure_time_UTC)
        self.arrival_time_UTC = self.strip_info("aTimeUTC")
        self.arrival_time = self.convert_timestamp(self.arrival_time_UTC)
        self.deep_link = self.strip_info("deep_link")
        self.duration= self.strip_info("fly_duration")
        self.transfer = self.strip_info("transfers")
        self.routes= self.strip_info("routes")
        self.airlines= self.strip_info("airlines")
        
    def strip_info(self, arg):
        return self.flight_data[arg]
        
    @staticmethod
    def convert_timestamp(timestamp):
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        conv_timestamp=timestamp.astimezone(pytz.timezone("Australia/Melbourne"))
        return conv_timestamp.strftime('%d/%m/%y %H:%M:%S')
        
    @staticmethod
    def convert_to_price(price):
        return f"${'{:.2f}'.format((price))} AUD"