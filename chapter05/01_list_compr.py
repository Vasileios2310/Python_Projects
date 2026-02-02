list_of_ints = [1,2,3,4,5,6,7]

# use a list comprehension to square each number in the list

squared_list_compr = [pow(number , 2) for number in list_of_ints]

print(f"squared list is : {squared_list_compr}")

# use map with a lambda 
squared_list_map = list(map(lambda number : number**2 , list_of_ints))
print(f"map list is : {squared_list_map}")


def square_function(num):
    return num ** 2


filtered_nums_list = [square_function(num) for num in list_of_ints if num % 2 == 0]
print(f"map list is : {filtered_nums_list}")

filtered_squared_map_filter = list(map(lambda num : num ** 2 , filter(lambda x : x % 2 == 0 , list_of_ints)))
print(filtered_squared_map_filter)