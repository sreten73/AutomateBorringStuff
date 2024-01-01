# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(addedItems):
    num =[]
    key = []
    dict = {}
    for j in range(len(addedItems)):
        k = 0
        #print(j+1 , addedItems[j])
        #print(j, addedItems[0:j])
        if addedItems[j] not in addedItems[0:j]:
            for i in range(len(addedItems)):
                if addedItems[j] == addedItems[i]:
                    k+=1
            key.append(addedItems[j])
            #print(k)
        if k != 0 :
            num.append(k)
    for k in range(len(num)):
        dict[key[k]] = num[k]
    #print(num)
    #print(key)
    return dict


display_inventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv1 = addToInventory(dragonLoot)
print(inv1)
print(inv)
inv2={}
for k in set(inv1):
    inv2[k]=inv1.get(k, 0) + inv.get(k, 0)

print(inv2)

display_inventory(inv2)
