from typing import List , Any

my_list = [1,2, "Hello" , [3,4,5]]

def append_to_list(li: List[Any] , element : Any) -> None:
    """Appends an element ot the provided List
    
    Parameters:
        li (List[Any]) : the list which the e;ement will be appended
        element (Any) : the element to append to the list
    """
    li.append(element)
    
    
def main():
    append_to_list(my_list , "Hello World")
    print(my_list)
    
    
    
if __name__ == "__main__":
    main()