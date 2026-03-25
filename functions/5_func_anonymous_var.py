funcs = [lambda x, n =n : x + n for n in range(5)]

for f in funcs:
    print(f(2))
    
    
print('-' *50)

# Default arguments are evaluated when the function is created, not when it’s called.
# x=x --> x is captured at definition time
x = 10
a = lambda y, x=x : x + y # a = 10 + y
#print(x)
x = 20
b = lambda y, x=x : x + y
#print(x)
print(a(10))
print(b(10))