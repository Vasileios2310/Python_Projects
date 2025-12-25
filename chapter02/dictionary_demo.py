products = {
    1:"apples" ,
    2:"oranges" ,
    3:"bananas" , 
    4:"melons"
    }
print("Initial dictionary " , products)

products[15] = "APPLES"
print("Updated dictionary " , products)

print(products[3])

products[2] = "milk"
print("Updated dictionary " , products)

del products[4]
print("Updated dictionary after deletion " , products)

removed_products = products.pop(100 , "Not found")
print("Updated dictionary after deletion " , removed_products)
print("Updated dictionary after deletion " , products)

#product = products.popitem()
#print(product)
#print(type(product))

key , value = products.popitem()
print(f"Key : {key} and Value {value}")
print(products)

key_to_check = 2

if key_to_check in products: 
    print(f"Product exists in {key_to_check}")
else:
    print(f"Product does not exists in {key_to_check}")

print("---KEYS---")    
for key in products.keys():
    print(key)

print("\n")

print("---VALUES---")   
for value in products.values():
    print(value)
    
for key in products:
    print(f"KEY : {key} has Value : {products[key]}")
print()

print("==============")
for key , value in products.items():
    print(f"Key {key} --> Value {value}")
print()