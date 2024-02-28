from fastapi import FastAPI, Query
from pydantic import BaseModel
from car import refuel_car, drive_car


app = FastAPI()

    
class CarDetails(BaseModel):
    combustion: int = 10
    tank_fuel: float = 10
    max_fuel: int = 20


cars = {}
    

@app.post("/create_car/{car_id}")
async def create_car(car_id: int, car: CarDetails):
    cars[car_id] = car
    return cars[car_id]


@app.get("/get_car/{car_id}")
async def get_car_by_id(car_id: int):
    return cars[car_id]


@app.put("/refuel_car/{car_id}")
async def refue_car(car_id: int, fuel: int | None = Query(default=1)):
    car = cars[car_id]
    car.tank_fuel = refuel_car(fuel, car.tank_fuel, car.max_fuel)
    if car.tank_fuel > car.max_fuel:
        car.tank_fuel = car.max_fuel
        return {"message": "Próbujesz zatankować za dużo"}
    return car

@app.put("/drive/{car_id}")
async def drive(car_id: int, kilometers : int | None = None):
    car = cars[car_id]
    car.tank_fuel = drive_car(car.tank_fuel, kilometers, car.combustion)
    if car.tank_fuel < 0:
        car.tank_fuel = 0
        return {"message": "Zabrakło paliwa"}
    return car