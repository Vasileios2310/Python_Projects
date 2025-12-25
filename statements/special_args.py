def standard_arg(arg):
    """_summary_
    the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword
    Args:
        arg (_type_): any value
    """
    print(arg)
    
def pos_only_arg(arg, /):
    """_summary_
     is restricted to only use positional parameters as there is a / in the function definition
    Args:
        arg (_type_): _description_
    """
    print(arg)
    
def kwd_only_arg(* , arg):
    """_summary_
    only allows keyword arguments as indicated by a * in the function definition
    Args:
        arg (_type_): _description_
    """
    print(arg)
    
def combined_example(pos_only, /, standard, *, kwd_only):
    """_summary_

    Args:
        pos_only (_type_): positional parameter
        standard (_type_): positional parameter or keyword arguments
        kwd_only (_type_): keyword argument
    """
    print(pos_only, standard, kwd_only)
    
standard_arg(2)
standard_arg(arg=8)

pos_only_arg(1)
#pos_only_arg(arg=8)

kwd_only_arg(arg=3)
combined_example(1 , 5 , kwd_only=9)
combined_example(1 , standard=5 , kwd_only=9)