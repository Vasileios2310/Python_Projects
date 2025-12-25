i = 5

def f(arg=i):
    print(arg)
    
i = 6
f()


def f_mutable(a , L=[]):
    """_summary_

    Args:
        a (_type_): integer
        L (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    L.append(a)
    return L

print(f_mutable(1))
print(f_mutable(2))
print(f_mutable(3))
    