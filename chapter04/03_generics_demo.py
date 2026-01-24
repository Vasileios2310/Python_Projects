from typing import Sequence , TypeVar , List , Any , Optional

T = TypeVar('T')
number = TypeVar("Number" , float , int)

def first(seq : Sequence[T]) -> T:
    if seq is None or len(seq) == 0:
        raise ValueError("Sequence is empty")
    return seq[0]


def last(seq : Sequence[T]) -> T:
    #if seq is None or len(seq) == 0:
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[-1]

def count_truthy(elements : List[Any]) -> int:
    """Return 1 , if element is truthy"""
    if elements is None:
        return 0
    total = 0
    for element in elements:
        if element:
            total += 1
    return total

def count_truthy2(elements : List[Any]) -> int:
    """Return 1 , if element is truthy"""
    return sum(1 for element in elements if element)

def len_str(s : Optional[str] = None) -> int:
    """Return len of str , otherwise 0"""
    return len(s) if s is not None else 0

def main():
    numbers = [1,2,3,4,5,6,0]
    print("First number" , first(numbers))
    print("Last number" , last(numbers))
    
    try:
        print("First num  in empty list" , first([]))
    except ValueError as e:
        print(e)
    
    mixed_values = [0 , True , False , None , 100 , 'HELLO']
    
    print("Truthy count" , count_truthy(mixed_values))
    print("Truthy count 2" , count_truthy2(mixed_values))
    
    print("Length of 'Hello'" , len_str('Hello'))
    print("Length of None" , len_str(None))
    
    
    
if __name__ == "__main__":
    main()
