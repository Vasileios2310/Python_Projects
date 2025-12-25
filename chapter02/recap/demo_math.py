def math_abs(x):
    """_summary_

    Args:
        x (_type_): integer positive or negative

    Returns:
        _type_: integer only postive
    """
    if x < 0 :
        return -x
    else:
        return x
    
x = math_abs(-5)
print(x)

x = math_abs(12)
print(x)

print("---------factorial-----------")

def factorial(x):
    """_summary_

    Args:
        x (_type_): integer positive or negative

    Returns:
        _type_: integer only postive
    """
    
    if x < 0 :
        return 'error : negative nimber'
    else:
        fact = 1
        for i in range(1 , x + 1):
            fact *= i
    return fact

x = factorial(5)
print(x)

x = factorial(-5)
print(x)

print("---------Power-----------")

def power(a , b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    if int(b) != b:
        print('error : not supported')
    elif b == 0:
        return 1
    elif b == 1:
        return a
    elif b > 1:
        p = 1
        for i in range(b):
            p *= a
        return p
    elif a == 0 and b < 0:
        return'error : division by zero'
    else:
        p = 1
        for i in range(-b):
            p /= a
        return p 
    
x = power(5 , 0)
print(x)

x = power(12 , 2)
print(x)

x = power(5 , -2)
print(x)

x = power(0, 0)
print(x)

x = power(0, -2)
print(x)