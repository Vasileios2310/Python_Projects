from typing import TypeVar

# declares generic type variables
T = TypeVar('T')

Number = TypeVar("Number" , int , float)

def add_numbers(a : Number , b : Number) -> Number:
    """
    Adds two numbers and returns the result
    
    Args:
        a (Number) : the first number
        b (Number) : the second number
    
    Returns :
        the sum of two numbers
    """
    
    if not (isinstance(a, (int , float)) and isinstance(b , (int , float))):
        raise TypeError("Both a and b must be integers or float")
    return a + b

def main():
    try:
        int_sum = add_numbers(10 , 20)
        print(f"int sum {int_sum}")
        
        float_sum = add_numbers(10.5 , 20.3)
        print(f"float sum {float_sum}")
        
        mix_sum = add_numbers(10.3 , 20)
        print(f"mix sum {mix_sum}")
        
        fail_sum = add_numbers("hello " , "world")
        print(f"fail sum {fail_sum}")
    except TypeError as ex:
        print(ex)
        
    
if __name__ == "__main__":
    main()