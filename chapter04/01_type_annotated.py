def my_add(a: float | int , b : float | int) -> float | int:
    """
    Adds two numbers and returns the results
    
    Args:
        a (int , float) --> the first number
        b (int , float) --> the second number
        
    Returns:
        int | float : the sum of a and b
    """
    if not (isinstance(a, (int , float)) and isinstance(b , (int , float))):
        raise TypeError("Both a and b must be integers or float")
        
    
    return a + b
    
    
def main():
    try:
        print(my_add(10 , 20))
        print(my_add(1.4 , 3.2))
        print(my_add(17.3 , 3))
        print(my_add(13, 12.2))
        
        print(my_add("Hello" , "World"))
    except TypeError as ex:
        print(ex)
        
    print("Annotations" , my_add.__annotations__)

if __name__ == "__main__":
    main()