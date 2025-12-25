def sum10(a , b):
    """_summary_

    Args:
        a (_type_): integer
        b (_type_): integer

    Returns:
        _type_: integer
    """
    sum = 0
    for i in range(a , b+1):
        sum += i
    return sum

x = sum10(1,10)
print(x)