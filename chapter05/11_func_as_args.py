def calculator(num1 , num2 , operation):
    try:
        return operation(num1  , num2)
    except TypeError as e:
        print(f"Error : {e} . Ensure the operation is a function taking two arguments")
        return None
        

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    if n2 == 0:
        raise ValueError('Division by zero is not allowed')
    return n1 / n2

def average (*args):
    return sum(args) / len(args)

def main():
    print("Addition : " , calculator(3 , 5 , add))
    print("Subtraction : " , calculator(3 , 5 , subtract))
    print("Multiplication : " , calculator(3 , 5 , multiply))
    print("Division : " , calculator(3 , 5 , divide))
    print("Average : " , calculator(3 , 5 , average))
    
if __name__ == "__main__":
    main()