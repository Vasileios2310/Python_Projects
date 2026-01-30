def fibo(n : int) -> int:
    """
    Parameters: An integer number
            
    Returns: The fibonaci recirsive
        
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibo(n - 1) + fibo(n - 2)

def main():
    try:
        
        n = int(input('Please insert a positive integer : '))
        print(f"fibo {n} = {fibo(n)}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        
if __name__ == "__main__":
    main()