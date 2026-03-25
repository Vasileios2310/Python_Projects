add = lambda x, y : x + y

x = add(2,3)
print(x)

y = add('hello' , 'world')
print(y)

z = add([1,2] , [3,4])
print(z)


names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder', 'Guido van Aberhen']

# 1. Splits the full name into words:
# 2. Takes the last word: sort by last name
# 3. Makes everything lowercase
new_names = sorted(names , key=lambda name: name.split()[-1].lower())
print(new_names)