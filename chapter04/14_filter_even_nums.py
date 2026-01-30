my_list = list(range(1 , 31))
            
even_numbers = [num for num in my_list if num % 2 == 0]
print(even_numbers)

even_numbers2 = filter(lambda x : x % 2 == 0 , my_list)
print(even_numbers2)

for num in even_numbers2:
    print(num , end=" ")
print()

print('---------returns an iterator-------')
# even_numbers2 is already exhausted.
# Iterators can be looped over once
for num in even_numbers2:
    print(num , end=" ")
print()

even_numbers_to_list = list(filter(lambda x : x % 2 == 0 , my_list))
print(even_numbers_to_list)