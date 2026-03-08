class Person:
    def __init__(self , name):
        self._name = name
        
    def get_name(self):
        print("Getting name" , end=": ")
        return self._name
    
    def set_name(self , value):
        if not isinstance(value , str):
            raise ValueError("Name must be a string")
        print("Setting name" , end=": ")
        self._name = value
        
    def del_name(self):
        print("Delete name")
        del self._name
        
    name = property(get_name , set_name , del_name , "This is the 'name' property")
    
def main():
    john = Person("John")
    print(john.name)
    
    john.name = "Alice"
    print(john.name)
    
    del john.name
    
    john.friends = []
    john.friends.append("Bob")
    john.friends.append("Dylan")
    
    print("Printing my friends")
    for friend in john.friends:
        print(f" - {friend}")
    
    
if __name__ == '__main__':
    main()