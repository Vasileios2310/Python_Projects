from collections import deque

def display_garage(garaze : deque) -> None:
    """
    Displays the current state of the garaze
    Params:
        garage (deque) : The dwque representation of the garaze
    Returns:
        None
    """
    if garaze:
        print('Current state is')
        for i , car in enumerate(garaze , 1):
            print(f"In position {i} --> {car}")
    else:
        print('\ngaraze is empty')
        

def add_car_to_garaze(garaze : deque , max_capacity : int) -> None:
    """
    Adds a car to the garaze if there is free space
    
    Params:
        garaze : (deque) --> the deque representation 
        max_capacity : (int) -> the maximum capacity of the cars the garaze can hold
        
    Returns:
        None
    """
    if len(garaze) < max_capacity:
        car_id = input('Enter the license plate')
        garaze.append(car_id)
        print(f"{car_id} is in the garaze")
    else:
        print(f"The garaze is full!!")
        
def remove_car_to_garaze(garaze : deque) -> None:
    """
    Removes the first car from the garaze if it is not empty
    
    Params:
        garaze : (deque) --> the deque representation 
        
    Returns:
        None
    """
    if garaze:
        car_left = garaze.popleft()
        print(f"{car_left} left from the garaze")
    else:
        print("No cars to remove")
        
def main():
    garaze = deque()
    max_capacity = 5
    
    while True:
        print("\nOptions")
        print("1. Add a car to the garaze")
        print("2. Remove the first car from the garaze")
        print("3. Display the state of the garaze")
        print("4. Exit")
    
        try:
            choice = int(input("Please give a choice between 1-4"))
        except ValueError:
            print("invalid value")
            continue
        
        match choice:
            case 1:
                add_car_to_garaze(garaze , max_capacity)
            case 2:
                remove_car_to_garaze(garaze)
            case 3:
                display_garage(garaze)
            case 4:
                print("Goodbye")
                break
            case _:
                print("Invalid choice")
             
        
if __name__ == "__main__":
    main()