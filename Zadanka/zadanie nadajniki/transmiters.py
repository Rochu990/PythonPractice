import math

t1 = (6, 11, 4)
t2 = (8, 17, 3)
t3 = (19, 19, 2)
t4 = (19, 11, 4)
t5 = (15, 7, 6)
t6 = (12, 19, 4)
start_point = (0, 0)
end_point = (19, 14)

transmiters =  [t2, t3, t5, t4, t1, t6]

def point(point: tuple[int, int], transmiter: list[tuple[int, int, int]]) -> bool:
    result = []
    for t in transmiter:
        if (((t[0] - point[0]) ** 2 + (t[1] - point[1]) ** 2) <= (t[2] ** 2)):
            result.append(t)
    return result

def transmiter_range(x: tuple[int, int, int], y: tuple[int, int, int]) -> bool:
    S = round(math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2), 2)
    return (abs(y[2] - x[2])) < S < abs(y[2] + x[2])

def range_path(data: list[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    path = []
    for n in data:
        for m in data:
            path.append(n)
            path.append(m)
    return set(path)

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