from functools import reduce

my_ints = [1,2,3,4,5]

# return result 1 * 2 * 3 * 4 * 5

result = reduce(lambda x,y : x * y , my_ints , 1)
print(f"result is : {result}")

result2 = reduce(lambda x,y : x + y , my_ints , 0)
print(f"result2 is : {result2}")