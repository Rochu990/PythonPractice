
def refuel_car(fuel: int, tank_fuel: int, max_fuel: int):
    tank_fuel = tank_fuel + fuel
    return tank_fuel

def drive_car(tank_fuel: int, kilometers: int, combustion: int):
    fuel= (kilometers / 100) * combustion
    tank_fuel = round((tank_fuel - fuel), 2)
    return tank_fuel

print(drive_car(10, 200, 10))
