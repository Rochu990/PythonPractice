# Masz plecak o pojemności 20 kg.
# Masz zegarek o wadze 3 kg i wartości 7 zł.
# Masz bransoletkę o wadze 2 kg i wartości 3 zł.
# Kolczyki o wadze 1 kg i wartości 2 zł.
# Jak zapakować plecak, żeby był najdroższy ?
# Napisz funkcję, która zwróci listę itemków, które stworzą plecak z najwyzszą wartością.

from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: int
    value: int


items = [Item('zegarek', 3, 7), Item('bransoleta', 2, 3), Item('kolczyki', 1, 2)]
capacity = 20


# def backpack(items, capacity, result_by_name: [], result_by_value: []):
#     for i in items:
#         if capacity - i.weight < 0:
#             break
#         else:
#             backpack(items, capacity - i.weight, result_by_name + [i.name], result_by_value + [i.value])
#     print(result_by_value, result_by_name)

def backpack(items, cap):
    result = []
    if not items:
        return []
    while True:
        added = False
        for item in items:
            if item.weight <= cap:
                added = True
                cap -= item.weight
                result.append(item.name)
        if not added:
            break
    return result


