import math

class StartPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    

class EndPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Transmiter:
    def __init__(self, x: int, y: int, range: int):
        self.x = x
        self.y = y
        self.range = range

    

# start_point = StartPoint(10,10)
# t1 = Transmiter(6, 11, 4)
# t2 = Transmiter(8, 17, 3)
# t3 = Transmiter(19, 19, 2)
# t4 = Transmiter(19, 11, 4)
# t5 = Transmiter(15, 7, 6)
# t6 = Transmiter(12, 19, 4)
# end_point = EndPoint(19, 14)

t1 = (6, 11, 4)
t2 = (8, 17, 3)
t3 = (19, 19, 2)
t4 = (19, 11, 4)
t5 = (15, 7, 6)
t6 = (12, 19, 4)




def transmitter_range(x, y):
    S = (y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2
    S = round(math.sqrt(S), 2)
    if (abs(y[2] - x[2])) < S < abs(y[2] + x[2]):
        return True

def start_point_transmiter(x, y):
    if (x[0] - y[0]) ** 2 - (x[1] - y[1]) ** 2 <= x[2]:
        return True

def end_point_transmiter(x, y):
    if (x[0] - y[0]) ** 2 - (x[1] - y[1]) ** 2 <= x[2]:
        return True


        
                
                
           
  
            








# t1 = (6, 11, 4)
# t2 = (8, 17, 3)
# t3 = (19, 19, 2)
# t4 = (19, 11, 4)
# t5 = (15, 7, 6)
# t6 = (12, 19, 4)

# data = [t1, t2, t3, t4, t5, t6]

# connected_transmiters = []

# def transmitter_range(x):
#     for t in x:
#         S = (t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2
#         S = round(math.sqrt(S), 2)
#         if (abs(t[2] - t[2])) < S < abs(t[2] + t[2]):
#             return True
        
# print(transmitter_range(data))
        