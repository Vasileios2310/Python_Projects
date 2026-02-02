from functools import reduce


n = int(input('Please give an int : '))

print(f"Facto of {n} calculations:")

result = reduce(lambda x , y : x * y , range(1 , n+1))
print(f"{n}! = " , result)

# print and mul
def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

new_result = reduce(print_and_multiply , range(1,n+1))
print(new_result)

print('-----------------')
result2 = reduce(lambda x , y: print(f"{x} * {y} = {x * y}") or x * y , range(1 , n + 1) )
print(f"result2 : {result2}")