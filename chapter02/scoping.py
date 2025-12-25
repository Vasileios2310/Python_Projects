import random

random_numbers = []

# for loop to generate 10 numbers
for _ in range(10):
    num = random.randint(1,100)
    random_numbers.append(num)
print(random_numbers)

for num in random_numbers:
    if num % 2 == 0:
        even = num
        
        
print(f"The last item of list is : {num}")
print(f"The last 'even' item of the list is: {even} ")