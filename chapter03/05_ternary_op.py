def compare_integers(a,b):
    
    if a == b:
        print("Equals")
    elif a > b:
        print("First number is grater than second")
    else:
        print("First number is less than second")

def main():
    
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError : 
        print("Invalid integer")
        return
        
    compare_integers(a,b)
    
    result = "Positive" if a > 0 else "Non Positive"
    print(result)
    
    res = (
        "Equals" if a == b else
        "First number is grater than second" if a > b else
        "First number is less than second" 
    )
    
    print(res)
if __name__ == "__main__":
    main()