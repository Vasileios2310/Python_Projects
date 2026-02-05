def test_args_func(pos_args1 , pos_args2 , opt_arg1 = None , opt_arg2 = None , *args , **kwargs):
    """
        Function demonstates the usage of positional , optional , additional positional args(*args) 
        and additional keyword arguments (**kwargs).
        
        Parameters :
            pos_args1 : the first positional argument
            pos_args2 : the second positional argument
            opt_arg1 : the first optional argument
            opt_arg2 : the second optional argument
            *args : Varargs
            **kwargs : Keyword arguments
    """ 
    print(f"pos_arg1 : {pos_args1}")
    print(f"pos_arg2 : {pos_args2}")
    print(f"opt_arg1 : {opt_arg1}")
    print(f"opt_arg2 : {opt_arg2}")
    
    if args:
        print('Additional positional arguments')
        for arg in args:
            print(arg)
            
    if kwargs:
        print('Additional keyword arguments')
        for key , val in kwargs.items():
            print(f"{key} : {val}")
            

def main():
    print('first')
    test_args_func("Hello" , "World" , opt_arg1=100 , opt_arg2=200)
    print('second')
    test_args_func("Hello" , "World" , opt_arg1=10 , keyw_arg1 = "Python" , keyw_args2 = "Android")
    print('third')
    test_args_func(
        "Hello" , "WORLD" ,  # pos_args1 , pos_args2
        100 , 200 ,          # opt_args1 , opt_args2
        300, 400   ,         # *args
        kwargs1 = "PYTHON" , kwargs2 = "DEEP LEARNING"
    )

if __name__ == '__main__':
    main()