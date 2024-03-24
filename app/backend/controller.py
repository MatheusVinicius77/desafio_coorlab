from fastapi import APIRouter, HTTPException
from model import Transport, TransportDB
from utils import conver_string_to_date
import os

db_file_path =  os.path.join(os.path.dirname(os.getcwd()), 'data.json')
router = APIRouter()

db = TransportDB(db_file_path)

@router.get("/transports/")
def read_transports():
    return db.transports


@router.get("/transports/{destination}/{date}")
def read_transports(destination:str, date:str):
    matching_destination_transports = [transport for transport in db.transports if transport.city.lower() == destination.lower()]
    travel_date = conver_string_to_date(date)

    print(matching_destination_transports)
    if matching_destination_transports:
        return matching_destination_transports
    raise HTTPException(status_code=404, detail=f"No transports found for destination: {destination}")
