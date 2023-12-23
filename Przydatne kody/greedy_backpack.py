# Masz plecak o pojemności 20 kg.
# Masz zegarek o wadze 3 kg i wartości 7 zł.
# Masz bransoletkę o wadze 2 kg i wartości 3 zł.
# Kolczyki o wadze 1 kg i wartości 2 zł.
# Jak zapakować plecak, żeby był najdroższy ?
# Napisz program, który to policzy, przy założeniu że podajesz:
# a. wielkość plecaka,
# b. kolejne przedmioty (waga, cena)

def backpack(weights: list[int], values: list[int], capacity: int):
   def items(x: int, y: int):
      if x == len(weights):
         return 0
      result = items(x + 1, y)
      if y >= weights[x]:
         result = max(result, items(x, y - weights[x]) + values[x])
      return result
   return items(0, capacity)

weights = [3, 2, 1]
values = [7, 3, 2]
capacity = 5



print(backpack(weights, values, capacity))
