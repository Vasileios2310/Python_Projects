for n in range(2,10):
    for x in range(2 , n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break
        
print('-------')

for num in range(2,10):
    if num % 2 == 0:
        print(f"Found and even number {num}")
        continue
    print(f"found and odd number {num}")