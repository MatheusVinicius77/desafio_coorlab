from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/")
def read_items():
    return {"Api running"}