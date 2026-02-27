def frange(start , stop , step):
    """
        yield --> function becomes generator --> it gives back one to one the values, not all together
    """
    x = start
    while x < stop:
        yield x # function becomes generator
        x += step
 
 
   
for n in frange(0.1 , 5 , 0.5):
    print(n)
    
print(list(frange(0 , 1 , 0.125)))

print('-' * 60)


def countdown(n):
    while n > 0:
        yield n
        n -= 1
    print('Done')
    
c = countdown(5)
print('Starting to count from ',next(c))
print('Starting to count from ',next(c))
print('Starting to count from ',next(c))
print('Starting to count from ',next(c))
print('Starting to count from ',next(c))