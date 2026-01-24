def my_add(*args: int ) -> int:
    """
    Calculate the sum of arbitary number of integers
    
    Parameters:
        *args (int) : A variable - length argument list of integers
        
    Returns:
        int: the sum of provided integers
    """
    return sum(args)


def my_average(*args: int ) -> float:
    """
    Calculate the average of an arbitary number of integers
    
    Parameters : 
        *args (int) : A variable - length argument list of integers
        
    Returns:
        float : the average of the provided integers
    """
    if not args:
        return 0
    return sum(args) / len(args)


def main():
    ages = [12,22,33,44,55]
    print("Average age: " , my_average(*ages))
    print("Average age: " , my_average(15,25))
    
if __name__ == "__main__":
    main()