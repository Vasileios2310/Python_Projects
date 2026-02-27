import numpy as np

# Python Lists
# lists are the built-in data structure that serves as a dynamic array.
# Lists are ordered, mutable, and can contain elements of different types.
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x *2)
# print(x + 10)  --> can only concatenate list (not "int") to list
print(x+y)

# Numpy Arrays
# An array is a data structure that stores elements of the same data type in contiguous memory locations, 
# making it efficient for numerical operations. Arrays require the array module to be used
ax = np.array([1,2,3,4])
bx = np.array([5,6,7,8])

print(ax*2)
print(ax + 10)
print(ax + bx)


print(np.sqrt(ax))
print(np.sqrt(bx))


grid = np.zeros(shape = (10000 , 10000), dtype = float)
grid += 10
print(grid)
print('-' * 40)
a = np.array( [
               [1 , 2 , 3 , 4] ,
               [5 , 6 , 7 , 8] ,
               [9 , 10 , 11 , 12]
               ]
            )

print('select second row ', a[1])
print('select first columv ',a[:,1])
print('select second row - third columb',a[1,2])

a[1:3 , 1:3] += 10
print(a)
