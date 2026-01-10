def calculate_sum_and_product(upper_bound):
    total_sum = 0
    total_product = 1
    
    for i in range(1 , upper_bound + 1):
        total_sum += i
        total_product *= i
     
    # tuples
    # return (total_product , total_sum) 
    return total_product , total_sum

def main():
    
    try:
        num = int(input("Please enter a positive number"))
        if num <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number")
        return
       
    my_sum , my_product = calculate_sum_and_product(upper_bound=num)
    print(f"Sum (1 - {num}) = {my_sum}")     
    print(f"Product (1 - {num}) = {my_product}") 
        
    #print(type(calculate_sum_and_product(upper_bound=num)))
    #t = calculate_sum_and_product(upper_bound=num)
    #print(f"Sum (1 - {num}) = {t[0]}")     
    #print(f"Product (1 - {num}) = {t[1]}")      
        
            
if __name__ == "__main__":
    main()