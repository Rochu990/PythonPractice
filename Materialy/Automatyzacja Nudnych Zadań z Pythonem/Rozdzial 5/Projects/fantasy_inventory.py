stuff = {"rope": 1, "torch": 6, "gold_coins": 42, "dagger": 1, "arrow": 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(k, v)
    print("Total items amount: {}".format(item_total))

display_inventory(stuff)
