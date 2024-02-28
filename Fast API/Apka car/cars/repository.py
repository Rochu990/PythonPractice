class Repository:

    def __init__(self):
        self.cars = {}

    def add(self, car):
        self.cars[car.id] = car

    def delete(self, id):
        del self.cars[id]

    def get(self, id):
        return self.cars[id]