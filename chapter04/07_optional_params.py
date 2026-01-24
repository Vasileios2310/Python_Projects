def my_add(a: int , b : int , c: int = 0) -> int:
    """
    Calculates the sum of two or three integers.
    
    Parameters:
        a (int) : the first number to add
        b (int) : the second number to add
        c (int , optional) : the third number to add , defaults to 0 if not provided
        
    Returns:
        int: the sum of provided numbers
    """
    return a + b + c

def my_add2(a: int = 0 , b : int = 0 , c: int = 0):
    return a + b + c
    

def main():
    print(f"my_add (10 , 20) = {my_add(10 , 20)}" )
    print(f"my_add (10 , 20 , 30) = {my_add(10 , 20 , 30)}" )
        
    print(f"my_add2 (10 , 20) = {my_add2(10 , 20)}" )
    print(f"my_add (10 , 20 , 30) = {my_add2(10 , 20 , 30)}" )
    
    print(my_add2(c = 130))
    
if __name__ == "__main__":
    main()