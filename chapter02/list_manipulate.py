fruits = ["banana" , "apple" , "mango" , "apple"]
print(f"Initial list of fruits is {fruits}")

fruits.append("Berry")
print(f"Updated list is now {fruits}")

fruits.append(["Grapes" , "Fig"])
print(f"Updated list is now a new nested list {fruits}")

fruits.insert(2 , "APPLES")
print(f"Updated list is now a new nested list {fruits}")

fruits[0] = "Melon"
print(f"Updated list is now {fruits}")

print(fruits[1:3])
fruits[1:3] = ["A" , "B"]
print(f"Updated list is {fruits}")

removed_items = fruits.pop(1)
print(f"Item to remove {removed_items}")
print(f"Updated list is : {fruits}")

new_removed_item = fruits.remove("mango")
print(f"Item to remove {new_removed_item}")
print(f"Updated list is : {fruits}")

pos = fruits.index("Berry")
print(f"In position : {pos} exists fruit {fruits[pos]}")