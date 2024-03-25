from datetime import datetime, timedelta


def convert_hours_string_to_int(hours_string):
    return int(hours_string.split('h')[0])


def conver_string_to_date(date:str):
    return datetime.strptime(date, '%Y-%m-%d').date()


def convert_price_to_float(price_string):
    # Remove o símbolo R$ e converte para float
    return float(price_string.replace("R$", "").replace(",", "."))

def extract_hours(transport):
    return int(transport.duration.replace('h', ''))

def diff_days(date1, date2):
    return abs((date2 - date1).days)



def get_best_comfortable_travel(travels,chosen_date, travel_type):
    weight_diff_days = 0.2
    weight_cust = 0.1
    weight_duration = 0.7
    best_travel = None
    best_proportion = float('inf')

    for travel in travels:
        days_diff = diff_days(chosen_date, travel.travel_date)
        proportion = (weight_diff_days * days_diff + 
                          (weight_cust) * convert_price_to_float(travel.price_confort)+
                          (weight_duration) * convert_hours_string_to_int(travel.duration)) / (weight_diff_days + weight_cust + weight_duration)
    
        proportion = (weight_diff_days * days_diff +  weight_cust * convert_price_to_float(travel.price_econ)) / (weight_diff_days + weight_cust)
        

        if proportion < best_proportion:
            best_proportion = proportion
            best_travel = travel
    
    return best_travel


def get_best_travel(travels,chosen_date, travel_type):
    weight_diff_days = 0.3
    weight_cust = 0.7
    best_travel = None
    best_proportion = float('inf')

    for travel in travels:
        print(travel)
        days_diff = diff_days(chosen_date, travel.travel_date)
        proportion = (weight_diff_days * days_diff + weight_cust * convert_price_to_float(travel.price_econ)) / (weight_cust + weight_diff_days) 

        if proportion < best_proportion:
            best_proportion = proportion
            best_travel = travel
    
    return best_travel

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