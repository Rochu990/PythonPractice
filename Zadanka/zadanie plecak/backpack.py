from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: int
    value: int

    def __lt__(self, other):
        return self.valueWeightRatio() > other.valueWeightRatio()

    def valueWeightRatio(self):
        return self.value / self.weight


itemki = [
            Item("zegarek", 3, 7),
            Item("bransoleta", 2, 3),
            Item("kolczyki", 1, 2)
            ]

def bp(items, capacity):
    if items == []:
        return []
    else:
        result = []
        items.sort()
        smallest = items[0].weight
        for i in items:
            if i.weight < smallest:
                smallest = i.weight
        while capacity >= smallest:
            for i in items:
                while i.weight <= capacity:
                    capacity -= i.weight 
                    result.append(i.name)     
        return  result
   

print(bp(itemki, 20))







