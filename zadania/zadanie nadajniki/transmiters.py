import math
from dataclasses import dataclass

@dataclass
class Transmiter:
    x: int
    y: int
    range: int

@dataclass
class Point:
    x: int
    y: int

t1 = Transmiter(6, 11, 4)
t2 = Transmiter(8, 17, 3)
t3 = Transmiter(19, 19, 2)
t4 = Transmiter(19, 11, 4)
t5 = Transmiter(15, 7, 6)
t6 = Transmiter(12, 19, 4)
start_point = Point(10, 19)
end_point = Point(19, 14)

transmiters =  [t2, t3, t5, t4, t1, t6]

def point(point: tuple[int, int], transmiter: tuple[int, int, int]) -> bool:
    result = []
    for t in transmiter:
        if (((t.x - point.x) ** 2 + (t.y - point.y) ** 2) <= (t.range ** 2)):
            result.append(t)
    return result

def transmiter_range(x: tuple[int, int, int], y: tuple[int, int, int]) -> bool:
    S = round(math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2), 2)
    return (abs(y.r - x.r)) < S < abs(y.r + x.r)
  

def range_path(data: list[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    path = []
    for n in data:
        for m in data:  
            path.append(n)
            path.append(m)
    return path

def solution(start: tuple[int, int], end: tuple[int, int], data: list[tuple[int, int, int]]) -> bool:  
    solution_1 = False
    solution_2 = False
    path = range_path(data)
    for s in point(start, data):
        solution_1 = s in path   
    for e in point(end, data):
        solution_2 = e in path 
    return solution_1 == True and solution_2 == True
        
print(solution(start_point, end_point, transmiters)) 