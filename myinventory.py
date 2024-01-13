def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for key,value in inventory.items():
        print(str(value) + ' ' + key)
        item_total += value
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    a=[]
    for i in range(len(addedItems)):
        print(addedItems[i]) 
        for k,v in inventory.items():
            if addedItems[i] == k:
                inventory[k] = v + 1
        if addedItems[i] not in list(inventory.keys()):
            a.append(addedItems[i])
            inventory[addedItems[i]] = 1
        print(inventory, a)
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'dagger', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)