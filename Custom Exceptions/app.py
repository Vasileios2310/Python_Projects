from store import Inventory , Item , OutOfStockError

def main():
    inventory = Inventory()
    
    inventory.add_item(Item("Apple", 10)) ## apples will be 10 and after add 5
    inventory.add_item(Item("Banana", 5))
    inventory.add_item(Item("Apple", 5))
    
    print("Current Inventory")
    inventory.print_items()
    
    print("Remove an Apple")
    inventory.remove_item("Apple")
    
    print("Inventory after removing an apple")
    inventory.print_items()
    
    try:
        inventory.remove_item("orange")
    except ValueError as ex:
        print(ex)
        
    try:
        for i in range(7):
            inventory.remove_item("Banana")
    except OutOfStockError as ex:
        print(ex)
    

if __name__ == '__main__':
    main()