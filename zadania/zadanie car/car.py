# Napisz klasę Car, która ma 3 metody

# refuel → przyjmującą ilość litrów

# drive → przyjmującą ilość kilometrów

# ‌
# Zwróć uwagę na:
# * nie można jechać dalej, jeśli nie masz już paliwa
# * nie można zatankować więcej niż pojemność baku
# * Ważne!!! parametr do refuel(tankowania) to ilość LITRÓW, więc weź to pod uwagę.\
# Dopisać ile udało  mi się przejechać km z planowanej drogi jak skończy mi się paliwo

# Dopisać testy!
 
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
        fuel = (km / 100) * self.combustion
        self.tank_fuel = self.tank_fuel - fuel
        if self.tank_fuel < 0:
            self.tank_fuel = 0
        
             
    def details(self):
        if self.tank_fuel < 0:
            return 'spalanie {} objętość baku {}'.format(self.combustion, 0)
        else:
            return 'spalanie {} objętość baku {}'.format(self.combustion, self.tank_fuel)

car = Car(6, 30, 60)

print(car.details())
print(car.drive(700))
print(car.details())
print(car.refuel(1000))
# print(car.drive(100))
print(car.refuel(2))
print(car.details())
