import datetime
import pytz
from typing import Union


class Flight():
    def __init__(self, flight_data: dict) -> None:
        self.flight_data = flight_data
        self.origin_city = self.strip_info("cityFrom")
        self.origin_country = self.strip_info("countryFrom")["name"]
        self.origin = f"{self.origin_city}, {self.origin_country}"
        self.dest_city = self.strip_info("cityTo")
        self.dest_country = self.strip_info("countryTo")["name"]
        self.destination = f"{self.dest_city}, {self.dest_country}"
        self.price = self.convert_to_price(self.strip_info("price"))
        self.departure_time_UTC = self.strip_info("dTimeUTC")
        self.departure_time = self.convert_timestamp(self.departure_time_UTC)
        self.arrival_time_UTC = self.strip_info("aTimeUTC")
        self.arrival_time = self.convert_timestamp(self.arrival_time_UTC)
        self.deep_link = self.strip_info("deep_link")
        self.duration = self.strip_info("fly_duration")
        self.airlines = self.strip_info("airlines")

    def strip_info(self, arg: str) -> Union[dict, str]:
        return self.flight_data[arg]

    @staticmethod
    def convert_timestamp(timestamp: int) -> str:
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        time_zone = pytz.timezone("Australia/Melbourne")
        conv_timestamp = timestamp.astimezone(time_zone)
        return conv_timestamp.strftime('%d/%m/%y %H:%M:%S')

    @staticmethod
    def convert_to_price(price: int) -> str:
        return f"${'{:.2f}'.format((price))} AUD"
