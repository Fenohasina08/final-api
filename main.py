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

  
@app.get("/cars/{id}", response_model=Car)
def get_car(id: str):
     
    for car in CarsStockage:
        if car.identifier == id:
            return car
     
    raise HTTPException(status_code=404, detail=f"L'{id}' du voiture n'as pas été trouvé.")

