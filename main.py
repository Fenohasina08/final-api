from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

 
class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

 
CarsStockage: List[Car] = []

 
@app.get("/ping")
def ping():
    return "pong"

 
@app.post("/cars", status_code= 201)
def cars(car: Car):
    CarsStockage.append(car)
    return car

@app.get("/cars", response_model=List[Car])
def cars():
    return CarsStockage

