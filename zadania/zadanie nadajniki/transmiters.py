from dataclasses import dataclass


@dataclass
class Transmiter:
    x: int
    y: int
    r: int


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
transmiters = [t1, t2, t3, t4, t5, t6]

p_start = Point(10, 19)
p_end = Point(19, 14)


def transmiter_range(transmiter1: Transmiter, transmiter2: Transmiter) -> bool:
    centre = (
        (transmiter2.x - transmiter1.x) ** 2 + (transmiter2.y - transmiter1.y) ** 2
    ) ** (1 / 2)
    r = transmiter1.r + transmiter2.r
    return centre <= r


def point_in_transmiter_range(transmiter: Transmiter, point: Point) -> bool:
    centre = ((transmiter.x - point.x) ** 2 + (transmiter.y - point.y) ** 2) ** (1 / 2)
    return centre <= transmiter.r


def signal_range(start_point: Point, end_point: Point, transmiters: list) -> bool:
    end = []
    connected_transmiters = []

    for i in transmiters:
        if point_in_transmiter_range(i, start_point):
            connected_transmiters.append(i)

    for i in transmiters:
        if point_in_transmiter_range(i, end_point):
            end.append(i)

    for z in connected_transmiters:
        for i in transmiters:
            if i in connected_transmiters:
                continue
            elif transmiter_range(z, i):
                connected_transmiters.append(i)

    for i in end:
        return i in connected_transmiters

    return False


print(signal_range(p_start, p_end, transmiters))
