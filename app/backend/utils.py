from datetime import datetime, timedelta

def conver_string_to_date(date:str):
    return datetime.strptime(date, '%Y-%m-%d').date()

def extract_hours(transport):
    return int(transport.duration.replace('h', ''))

def get_closest_transport(travel_date,sorted_transports):
    closest_transport = None
    closest_transport_delta = timedelta(days=365)  # Definindo um valor inicial grande para a diferença de data
    for transport in sorted_transports:
        transport_date = calculate_transport_date(transport, travel_date)
        delta = abs(travel_date - transport_date)
        if delta < closest_transport_delta:
            closest_transport = transport
            closest_transport_delta = delta
    
    return closest_transport

def calculate_transport_date(transport, travel_date):
    hours = int(transport.duration.replace('h', ''))
    return travel_date + timedelta(hours=hours)