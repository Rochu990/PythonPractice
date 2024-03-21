import math

t1 = (6, 11, 4)
t2 = (8, 17, 3)
t3 = (19, 19, 2)
t4 = (19, 11, 4)
t5 = (15, 7, 6)
t6 = (12, 19, 4)
start_point = (10, 19)
end_point = (19, 14)

transmiters =  [t2, t3, t5, t4, t1, t6]

def point(point, transmiter):
    result = []
    for t in transmiter:
        if (((t[0] - point[0]) ** 2 + (t[1] - point[1]) ** 2) <= (t[2] ** 2)) == True:
            result.append(t)
    return result


def transmiter_range(x, y):
    S = round(math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2), 2)
    if (abs(y[2] - x[2])) < S < abs(y[2] + x[2]):
        return True
    else:
        return False
    
def range_path(data):
    path = []
    for n in data:
        for m in data:
            if transmiter_range(n, m) == True:
                if n not in path:
                    path.append(n)
                if m not in path:
                    path.append(m)
    return path


def solution(start, end, data):
    solution_1 = False
    solution_2 = False
    path = range_path(data)
    for s in point(start, data):
        if s in path:
            solution_1 = True
        else:
            solution_1 = False
    
    for e in point(end, data):
        if e in path:
            solution_2 = True
        else:
            solution_2 = False
    
    if solution_1 == True and solution_2 == True:
        return True
    else:
        return False
        

print(solution(start_point, end_point, transmiters)) 