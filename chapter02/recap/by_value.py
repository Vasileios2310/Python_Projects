def inc(x):
    print(x)
    x = x + 1
    print(x)
    


a = 3 
print(a)
inc(a)
print(a)

print("---------------------")

def f(x):
    x.append(4)

a = [1,2,3]
f(a)
print(a)     # [1, 2, 3, 4]   ← change
