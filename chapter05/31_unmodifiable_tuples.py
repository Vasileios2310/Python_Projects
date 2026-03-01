def main():
    """
        Tuples are unmodifiable but they can contain mutable objects
    """
    g = 1 , 2 , 3 , 4  #  --> g = (1 , 2 , 3 , 4 )
    
    print(f"Type of {type(g)}")
    
    my_tuple = (1 , 2 , [3 , "Hello World"] , "Siberian")
       
    # A tuple does not allow us to modify its elements directly, which is why my_tuple[2] = 100 fails. 
    # However, if one of the tuple’s elements is 
    # a mutable object, such as a list, we can modify the contents of that object without changing the tuple itself.
    try:     
        my_tuple[2] = 100
    except TypeError as ex:
        print("Error: " , ex)
        
    my_tuple[2][0] = 300
    
    print("Modified tuple:" , my_tuple)
    
if __name__ == '__main__':
    main()