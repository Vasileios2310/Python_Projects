import functools

def calculate(args : list[float] ) -> dict:
    """
    Generate functions to perform arithmetic operations on a list of numbers.
    
    Parameters:
        args(lists of floats): Lists of numbers to perform operations on
        
    Returns:
        dict : A dictionary of functions for add, sub , mul , average
    """
    
    def plus() -> dict:
        return functools.reduce(lambda x , y : x + y , args)
        
    def minus():
        return functools.reduce(lambda x , y : x - y , args )
        
    def mul():
        return functools.reduce(lambda x , y : x * y , args)
    
    def average():
        return sum(args) / len (args)
    
    return {
        "add" : plus,
        "subtract" : minus,
        "multiply" : mul,
        "average" : average
    }

def main() -> None:
    args = [5,4,3,2,1]
    operations = calculate(args)
    
    while True:
        print("Choose an operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Average")
        print("5. Exit")
        
        try:
            choice = int(input("Enter a choice 1 - 5 "))
        except ValueError:
            print("Invalid input")
            
        match choice:
            case 1:
                print("Additional result" , operations['add']())
            case 2:
                print("Subtraction result" , operations['subtract']())
            case 3:
                print("Multiplication result" , operations['multiply']()) 
            case 4:
                print("Average result" , operations['average']()) 
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid choice")
            
    
if __name__ == '__main__':
    main()