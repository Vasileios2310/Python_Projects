def myfunc():
    return 1,2,3

# return multiple values from a function, simply return a tuple
a,b,c = myfunc()

x = myfunc()

print(a)
print(b)
print(c)

# When calling functions that return a tuple, it is common to assign the result to multiple variables
print(x)