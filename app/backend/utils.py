from datetime import datetime

def conver_string_to_date(date:str):
    return datetime.strptime(date, '%Y-%m-%d').date()