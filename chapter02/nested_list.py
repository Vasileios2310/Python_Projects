items = [1 , 2 , 3.14 , True , "Hello World"]
    
for item in items:
    print(item , end=" ")
print()  


nested_list = [[1 , 2] , [3 , 4] , [5 , 6]]

print(f"Nested list is {nested_list}")

print(f"First index from nested list is {nested_list[0]}")

print(f"First element of secont nested list is {nested_list[1][0]}")

for outer_item in nested_list:
    for inner_item in outer_item:
        if inner_item % 2 == 0:
            result = inner_item
print(f"Final result is {result}")