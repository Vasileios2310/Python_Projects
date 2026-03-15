class Vehicle:
    """Anything that is aVehicle , should implement drive()"""
    def drive(self):
        raise NotImplementedError("Subclasses should implement 'drive' method")
    
class Car(Vehicle):
    def drive(self):
        print("Driving a car")
        
class Bicycle(Vehicle):
    def drive(self):
        print("Driving a bike")       

class Hoverboad:
    """ This class does not inherit from Vehicle.
        It still works because the object has a drive() method. Python only checks behavior, not lineage.
        This idea is called duck typing.
    """
    def drive(self):
        print("Hovering a hoverboad")       

class Boat(Vehicle):
    """
        There is no drive() method.
        So when Boat inherits from Vehicle, it inherits this: def drive(self):
    """
    def sail(self):
        print("Sailing a boat")       

def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} can not drive")
        
        
def main():
    my_car = Car()
    my_bicycle = Bicycle()
    my_hoverboard = Hoverboad()
    my_boat = Boat()
    
    drive_vehicle(my_car)
    drive_vehicle(my_bicycle)
    drive_vehicle(my_hoverboard)
    
    try:
        drive_vehicle(my_boat)
    except NotImplementedError as ex:
        print(e)
    
    
    
  
if __name__ == '__main__':
    main()