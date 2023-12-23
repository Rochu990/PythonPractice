# Masz plecak o pojemności 20 kg.
# Masz zegarek o wadze 3 kg i wartości 7 zł.
# Masz bransoletkę o wadze 2 kg i wartości 3 zł.
# Kolczyki o wadze 1 kg i wartości 2 zł.
# Jak zapakować plecak, żeby był najdroższy ?
# Napisz program, który to policzy, przy założeniu że podajesz:
# a. wielkość plecaka,
# b. kolejne przedmioty (waga, cena)

from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: int
    value: int


items = [Item('zegarek', 3, 7), Item('bransoleta', 2, 3), Item('kolczyki', 1, 2)]
cap = 5

def backpack(items, capacity, result_by_name: [], result_by_value: []):
    for i in items:
        if capacity - i.weight < 0:
            break
        else:
            backpack(items, capacity - i.weight, result_by_name + [i.name], result_by_value + [i.value])
    print(result_by_value)
            


            

print(backpack(items, cap, [], []))
