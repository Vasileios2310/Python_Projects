def factorial(n : int) -> int:
    """
    Parameters: An integer number
            
    Returns: The factorial of integer
        
    """
    if n < 0 : return 0
    if n in (0,1): return 1
    
    return n  *  factorial(n - 1)      

def main():
    n = int(input('Please insert a positive integer : '))
    
    print(f"{n}! = {factorial(n)}")
    
        
if __name__ == "__main__":
    main()