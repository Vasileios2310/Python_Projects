def f(ham: str , eggs: str = 'EGGS' ) -> str:
    print("Annotations" , f.__annotations__)
    print("Arguments", ham , eggs)
    return ham + 'and' + eggs
    
    
f('HAM')