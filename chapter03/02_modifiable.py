def print_id(variable_name , variable):
    print(f"id({variable_name}) = {id(variable)}")



def main():
    original_list = [1,2]
    new_list = original_list
    
    print_id("original list" , original_list)
    print_id("new list" , new_list)
    
    temp_list = [1,2]
    print_id("temp list" , temp_list)

if __name__ == "__main__":
    main()