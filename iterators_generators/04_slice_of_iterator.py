import itertools


c = range(10,200)

for x in itertools.islice(c , 10 , 200):
    print(x)
    
