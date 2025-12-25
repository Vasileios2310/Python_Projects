def func (n):
    if n == 0:
        return 1
    else:
        return n * func(n-1)
x = 5
print(f"{x}! = {func(x)}")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

insert_num = 10_000

if insert_num <= 0:
    print('Please insert a positive number')
else:
    print('Fibonacci recursive')
    for i in range(insert_num):
        print(fibonacci(i)) 