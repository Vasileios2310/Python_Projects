from math import sqrt
# ax**2 + by + c

a = float(input('Give me the a '))
b = float(input('Give me the b '))
c = float(input('Give me the c '))

if a == 0:
    if b != 0:
        y = -c/b
        print('There is only one solution' , y)
    elif c == 0:
        print('Each R is solution')
    else:
        print('No solution')
else:
    D = b**2 -4*a*c
    if D > 0:
        x1 = (-b + sqrt(D))/(2*a)        
        x2 = (-b - sqrt(D))/(2*a)  
        print('Solutions are ' , x1 , x2)
    elif D == 0:
        x = (-b + sqrt(D))/(2*a)
        print('Solution is ' , x)
    elif D < 0:
         c1 = -b/(2*a) + (sqrt(-D))*1j
         c2 = -b/(2*a) + (sqrt(-D))*1j
         print('Solutions are ' , c1 , c2)