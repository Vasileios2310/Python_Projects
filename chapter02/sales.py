fruits = ["banana" , "apple" , "mango" , "grapes"]

fruit_to_check = "Banana"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"So {fruit_to_check} is in list")
        break
else:
    print(f"{fruit_to_check} is not in list")
    
    
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in list'}")
