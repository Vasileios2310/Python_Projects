def print_id(variable_name , variable):
    print(f"id({variable_name}) = {id(variable)}")



def main():
    a = 10
    b = 10
    
    str1 = "Hello"
    str2 = 'Hello'
    
    print_id("a" , a)
    print_id("b" , b)
    
    print_id("str1" , str1)
    print_id("str2" , str2)

if __name__ == "__main__":
    main()