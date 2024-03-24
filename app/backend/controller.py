from fastapi import APIRouter, HTTPException
from model import Transport, TransportDB
from utils import conver_string_to_date, extract_hours
import os

db_file_path =  os.path.join(os.path.dirname(os.getcwd()), 'data.json')
router = APIRouter()

db = TransportDB(db_file_path)

@router.get("/transports/")
def read_transports():
    return db.transports




@router.get("/transports/comfortable/{destination}/{date}")
def get_most_comfortable(destination:str, date:str):
    # GET ALL TRANSPORTS FOR THAT DESTINATION
    matching_destination_transports = [transport for transport in db.transports if transport.city.lower() == destination.lower()]
    travel_date = conver_string_to_date(date)
    

    if matching_destination_transports:
        # SORTING ALL THE TRANSPORTS BY ITS DURATION
        sorted_transports = sorted(matching_destination_transports, key= extract_hours)
        
        # GETTING THE MOST COMFORTABLE 
        more_comfortable = sorted_transports[0]
        
        return more_comfortable
    
    raise HTTPException(status_code=404, detail=f"No transports found for destination: {destination}")



@router.get("/transports/economic/{destination}/{date}")
def get_most_economic(destination:str, date:str):
        matching_destination_transports = [transport for transport in db.transports if transport.city.lower() == destination.lower()]
        travel_date = conver_string_to_date(date)
        if matching_destination_transports:
            # SORTING BY ITS ECONOMIC PRICE
            sorted_transports = sorted(matching_destination_transports, key= lambda transport:transport.price_econ)
            more_economic = sorted_transports[0]
        
            return more_economic

        raise HTTPException(status_code=404, detail=f"No transports found for destination: {destination}")
        
