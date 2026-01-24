my_list = [1,2, "Hello" , [3,4,5]]

# shallow copy

new_list = my_list[:]

print("Are new_list and my_list the same obj : " , my_list is new_list)

new_list[0] = 100

print(f"my_list {my_list}")
print(f"new_list {new_list}")

print('---------------------------')


new_list[3][0] = 300
print(f"my_list {my_list}")
print(f"new_list {new_list}")
