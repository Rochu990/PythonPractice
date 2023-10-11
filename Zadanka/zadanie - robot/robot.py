
class Robot:

    def __init__(self, x: int, y: int, sight: str):
        self.x = x
        self.y = y
        self. sight = sight

    def position(self):
        return self.x, self.y
    
    def turn_right(self):
        if self.sight == "N":
            self.sight = "E"
        elif self.sight == "E":
            self.sight = "S"
        elif self.sight == "S":
            self.sight = "W"  
        elif self.sight == "W":
            self.sight = "N" 

    def turn_left(self):
        if self.sight == "N":
            self.sight = "W"
        elif self.sight == "W":
            self.sight = "S"
        elif self.sight == "S":
            self.sight = "E"  
        elif self.sight == "E":
            self.sight = "N"   
    
    def drive(self):
        if self.sight == "N":
            self.x += 1
        elif self.sight == "E":
            self.y += 1
        elif self.sight == "S":
            self.x -= 1  
        elif self.sight == "W":
            self.y -= 1  
    


robot = Robot(1, 1, "N")

print(robot.position())
robot.turn_left()
robot.drive()
robot.drive()
robot.drive()
print(robot.position())
