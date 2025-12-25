def pSquare50():
    """_summary_

    Returns:
        _type_: _description_
    """
    L = [x * x for x in range(1, 11)]
    T = [abs(y - 50) for y in L]
    return L,T.index(min(T))


A,a = pSquare50()
print(f"The perfect square list is {A} , in position {a} and is the number {A[a]}")
