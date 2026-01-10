def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    total = 0
    
    for digit in digits:
        total += int(digit) ** power 
    
    return n == total

def main():
    try:
        num = int(input("Please insert a number"))
    except ValueError:
        print("Invalid number")
        return
    
    if is_armstrong_number(num):
        print(f"{num} is armstrong number")
    else:
        print(f"{num} is not armstrong number")
        
if __name__ == "__main__":
    main()