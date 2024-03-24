import json
from utils import conver_string_to_date

class Transport:
    def __init__(self, id, name, price_confort, price_econ, city,duration,seat,bed,travel_date):
        self.id = id
        self.name = name
        self.price_confort = price_confort
        self.price_econ = price_econ
        self.city = city
        self.duration = duration
        self.seat = seat
        self.bed = bed
        self.travel_date = conver_string_to_date(travel_date)

    def __repr__(self):
        return f"Transport(id={self.id}, name='{self.name}', city='{self.city}', duration='{self.duration}')"
    
class TransportDB:
    def __init__(self, json_file):
        self.json_file = json_file
        self.transports = self.load_transports()

    def load_transports(self):
        try:
            with open(self.json_file, 'r') as f:
                transports_data = json.load(f)["transport"]
                return [Transport(**data) for data in transports_data]

        except FileNotFoundError:
            return []

    def save_transports(self):
        with open(self.json_file, 'w') as f:
            json.dump({"transport": [vars(transport) for transport in self.transports]}, f)

    
    