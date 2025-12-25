bag = {"eggs" , "apples" , "bananas" , "eggs"}

print("Initial bag" , bag)

bag.add("oranges")
print(f"After adding item , Set has {bag}")


item_to_remove = "eggs"
if item_to_remove in bag:
    bag.remove(item_to_remove)
    print(f"After removing item , Set has {bag}")

# iterate through the set
for item in bag:
    print(item)
    
    

    
