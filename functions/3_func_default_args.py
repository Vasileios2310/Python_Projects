# define a function or method where one or more of the arguments are optional and have a default value

def spam(a , b = 12):
    #return a,b
    print(a,b)

x = spam(1) ## 1,12
y = spam(1,122) ## 1,122

#print(x) --> needs return
#print(y) --> needs return

def spam2(a , b = None):
    if b is None:
        b = [1,2,3,4,5]
    return a , *b # take all elements of b and spread them out

z = spam2(11)
print(z)