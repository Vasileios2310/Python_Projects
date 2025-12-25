inventory = {'apples' : 400 , 'oranges' : 200 , 'mangos' : 25}

print(inventory)

del inventory['oranges']
print(inventory)

print(len(inventory))

print('apples' in inventory)

keys_view = inventory.keys()
print(keys_view)

values_view = inventory.values()
print(values_view)

items_view = inventory.items

for key in inventory:
    print(key)