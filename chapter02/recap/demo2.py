def outer():
    """_summary_
    """
    x = 2
    print('Now x = ', x)
    
    def inner():
        """_summary_
        """
        nonlocal x
        x = 5
        
    inner()
    
    print('And Now x = ' , x)
    
outer()