from abc import ABC , abstractmethod
# Python’s abc module means Abstract Base Class. 
# It lets you create classes that cannot be instantiated directly and that force subclasses to implement certain methods.
class AbstractStudentDAO(ABC):
    """Defines the Student DAO API,
       used for data storage operations and what operations must exist
       ABC --> class is abstract and you can not create objects from it
    """
    
    @abstractmethod
    def insert(self , student):
        raise NotImplementedError()
    
    @abstractmethod
    def update(self , student_id , student):
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self , student_id):
        raise NotImplementedError()
    
    
    @abstractmethod
    def get_one(self , student_id):
        raise NotImplementedError()
    
class StudentImpl(AbstractStudentDAO):
    """Defines how those operations actually work"""
    def __init__(self):
        """This creates a dictionary to store students
                key → student ID
                value → the full student data
        """
        self.students = {}
        
    def insert(self , student):
        student_id = student['id']  # Extract the ID from the dictionary.
        self.students[student_id] = student # store the student into the dictionary
        print(f"Inserted student with id : {student_id}")
        
    def update(self , student_id , student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with id: {student_id}")
        else:
            print(f"Student with id {student_id} not found")
        
    def delete(self , student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Deleted student with id: {student_id}")
        else:
            print(f"Student with id {student_id} not found")
        
    def get_one(self , student_id):
        return self.students.get(student_id , None) 

class InventorABC(ABC):
    
    @abstractmethod
    def add_item(self , item):
        """Add an item to the inventory"""
        pass        
  
    @abstractmethod
    def remove_item(self , item_to_remove):
        """Remove an item from the inventory"""
        pass 
    
class Inventory(InventorABC):
    def __init__(self):
        self.items = []
        
    def add_item(self , item):
        """Add an item to the inventory"""
        self.items.append(item)
        
    def remove_item (self , item_to_remove):
        """Remove item by name"""
        for item in self.items:
            if item.name == item_to_remove:
                self.items.remove(item_to_remove)
                print(f"Removed item: {item_to_remove}")
                return
        print(f"Item not found {item_to_remove}")

class Item:
    def __init__(self , name):
        self.name = name
        
    def __str__(self):
        return self.name
       
def main():
    student_impl = StudentImpl()
    student_impl.insert({'id' : 1 , 'name' : "Alice" })
    student_impl.insert({'id' : 2 , 'name' : "Bob"})
     
    student_impl.update(1 , {'id' : 1 , 'name' : "DYLAN"})
    
    print(student_impl.get_one(1))
    
    inventory = Inventory()
    item1 = Item("Laptop")
    item2 = Item("Phone")
    
    inventory.add_item(item=item1)
    inventory.add_item(item=item2)
  
if __name__ == '__main__':
    main()