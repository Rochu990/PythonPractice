from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Car:
    def __init__(self, combustion: int, tank_fuel: int, max_fuel: int):
        self.combustion = combustion
        self.tank_fuel = tank_fuel
        self.max_fuel = max_fuel
       
    def refuel(self, fuel):
        self.tank_fuel = self.tank_fuel + fuel
        if self.tank_fuel > self.max_fuel:
            print("Próbujesz zatankować za dużo")
            self.tank_fuel = self.max_fuel
        
        
    def drive(self, km):
        fuel_after_tank = self.tank_fuel
        fuel = (km / 100) * self.combustion
        self.tank_fuel = self.tank_fuel - fuel
        if self.tank_fuel < 0:
            self.tank_fuel = 0
        
             
    def details(self):
        if self.tank_fuel < 0:
            return 'spalanie {} objętość baku {}'.format(self.combustion, 0)
        else:
            return 'spalanie {} objętość baku {}'.format(self.combustion, self.tank_fuel)
        

class CarDetails(BaseModel):
    combustion: Optional[int]
    tank_fuel: Optional[int]
    max_fuel: Optional[int]


cars = {}
    

@app.post("/create_car/{car_id}")
def create_car(car_id: int, car: CarDetails):
    cars[car_id] = car
    return cars[car_id]


@app.get("/get_car/{car_id}")
def get_car_by_id(car_id: int):
    return cars[car_id]


@app.put("/refuel_car/{car_id}")
def refuel_car(car_id: int, fuel: int, car: CarDetails):
    cars[car_id] = car
    car.tank_fuel = car.tank_fuel + fuel
    if car.tank_fuel > car.max_fuel:
            return("Próbujesz zatankować za dużo")
    car.tank_fuel = car.max_fuel

    return cars[car_id]