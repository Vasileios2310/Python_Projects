from decimal import Decimal , localcontext

a = Decimal('4.2')
b = Decimal('1.9')

c = a + b 
print(c)

if (a + b) == Decimal('6.1') :  print(True) 
else: print(False)

print('-' * 30)

# to many digits
print(a / b)

# better now
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

# oups!!!
with localcontext() as ctx:
    ctx.prec = 100
    print(a / b)