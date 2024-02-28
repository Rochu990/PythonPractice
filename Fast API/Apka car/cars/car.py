import uuid

class Car:
    def __init__(self, combustion: int, tank_fuel: int, max_fuel: int):
        self.combustion = combustion
        self.tank_fuel = tank_fuel
        self.max_fuel = max_fuel
        self.id = uuid.uuid4()

    def refuel(self, fuel):
        self.tank_fuel = self.tank_fuel + fuel
        if self.tank_fuel > self.max_fuel:
            print("Próbujesz zatankować za dużo")
            self.tank_fuel = self.max_fuel
        return self.tank_fuel
        
        
    def drive(self, km):
        fuel = (km / 100) * self.combustion
        self.tank_fuel = self.tank_fuel - fuel
        if self.tank_fuel < 0:
            self.tank_fuel = 0
        return self.tank_fuel