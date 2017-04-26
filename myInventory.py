stuff = {'arrow': 105, 'gold coin': 42, 'light set': 1, 'bow': 6,
             'dagger': 1, 'mana potion': 12, 'hp potion': 23, 'SS': 1000}

def displayInventory(inventory):
    print('Inventory:')
    itemtotal = 0
    for i, j in inventory.items():
        print(str(j) + ' ' + i)
        itemtotal += j
    print('Total number of items: ' + str(itemtotal))

displayInventory(stuff)
