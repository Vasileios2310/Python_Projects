my_list = [1,2, "Hello" , [3,4,5]]


print("At the start")
for element in my_list:
    print(f"{element} : {id(element)}")
    
new_list = my_list * 2

print("Dublicated list")
print("Dublicated list: " , new_list)

new_list[0] = 100
print("Update list")
print("Updated list: " , new_list)

new_list[3][0] = 300
print("Updated list: " , new_list)

print("At the end")
for element in my_list:
    print(f"{element} : {id(element)}")