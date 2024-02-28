class Cars:
    
    def __init__(self, repository):
        self.repository = repository

    def refuel(self, id, fuel):
        car = self.repository.get(id)
        return car.refuel(fuel)
        
    def add(self, car):
        return self.repository.add(car)
        
    def drive(self, id, km):
        car = self.repository.get(id)
        return car.drive(km)
        
             
    