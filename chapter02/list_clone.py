def deleteHead(mylist):
    del mylist[0]
    
numbers = [5,7,9]
deleteHead(numbers)
print(numbers)

print('----')




a = [1,2,3]
b = a[:]

print(a)
print(b)

b = a
b[0] = 12

print(a)
print(b)