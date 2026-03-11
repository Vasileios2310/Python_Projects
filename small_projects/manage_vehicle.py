# Fleet Management System for a Transportation Company


# Vehicle Class
class Vehicle:
    """The Vehicle class describes a vehicle. It provides the methods
    depart, arrive, info, and the special method __str__."""

    def __init__(self, plate, brand, location, on_route=False, destination=None):
        """Vehicle constructor.
        Parameters: plate number, brand, and current location.
        Assumes the vehicle is not on a route (on_route=False) and destination=None."""
        self.__plate = plate
        self.__brand = brand
        self.__location = location
        self.__on_route = on_route
        self.__destination = destination

    def depart(self, destination):
        """The depart method describes the vehicle leaving.
        It sets the vehicle destination."""
        try:
            if destination:
                self.__destination = destination
                self.__on_route = True
            else:
                print("Please select a destination.")
        except ValueError as ex:
            print(ex)

    def arrive(self):
        """The arrive method describes the vehicle arriving.
        It updates the vehicle location."""
        self.__location = self.__destination
        self.__on_route = False
        self.__destination = None

    def info(self):
        """The info method returns a description of the vehicle."""
        if self.__location:
            return (f"Vehicle with plate {self.__plate}, brand {self.__brand}, "
                    f"current location: {self.__location}")
        else:
            return (f"Vehicle with plate {self.__plate}, brand {self.__brand}")

    def __str__(self) -> str:
        """__str__ returns the vehicle status:
        whether it is in the depot or on a route."""
        if self.__on_route:
            return f"Vehicle {self.__plate} is on route to {self.__destination}"
        else:
            return f"Vehicle {self.__plate} is in the depot at {self.__location}"

class Truck(Vehicle):
    """Truck inherits from Vehicle and represents trucks.
    Max load: 25 tons.
    Cost: 1.20€/km + 0.05€/km per ton of load."""

    MAX_LOAD = 25  # Maximum load in tons

    def __init__(self, plate, brand, location, load=MAX_LOAD):
        """Truck constructor.
        Parameters: plate, brand, location, and load in tons.
        If load exceeds the maximum allowed (25 tons),
        it prints a message and limits the load."""
        super().__init__(plate, brand, location)
        self.__load = load

        if self.__load > self.MAX_LOAD:
            print(f"Maximum load cannot exceed {self.MAX_LOAD} tons.")
            self.__load = self.MAX_LOAD

    def calculate_cost(self, distance):
        """Calculates transport cost.
        Cost = distance * (1.20 + 0.05 * load)"""
        total_cost = distance * (1.20 + 0.05 * self.__load)
        return total_cost

    def __str__(self):
        """__str__ returns the truck status.
        If the vehicle is on route, it also returns the load being carried."""
        status = super().__str__()

        if "on route" in status:
            return f"{status}, carrying load {self.__load} tons"
        else:
            return status

class Van(Vehicle):
    """Van inherits from Vehicle and represents vans for package transport.
    Max packages: 100.
    Cost: 0.80€/km + 0.02€/km per package."""

    MAX_PACKAGES = 100  # Maximum number of packages

    def __init__(self, plate, brand, location, packages):
        """Van constructor.
        Parameters: plate, brand, location, and number of packages.
        If packages exceed the maximum allowed (100),
        it prints a message and limits the number."""
        super().__init__(plate, brand, location)
        self.__packages = packages

        if self.__packages > self.MAX_PACKAGES:
            print(f"Maximum number of packages cannot exceed {self.MAX_PACKAGES}.")
            self.__packages = self.MAX_PACKAGES

    def calculate_cost(self, distance):
        """Calculates transport cost.
        Cost = distance * (0.80 + 0.02 * packages)"""
        total_cost = distance * (0.80 + 0.02 * self.__packages)
        return total_cost

    def __str__(self):
        """__str__ returns the van status.
        If the vehicle is on route, it also returns the number of packages."""
        status = super().__str__()

        if "on route" in status:
            return f"{status}, carrying {self.__packages} packages"
        else:
            return status


def main():

    # --- Truck Test ---
    print("=== Truck Test ===")
    truck1 = Truck("KHI-4521", "Mercedes Actros", "Patras", 66)
    print(truck1.info())
    print(truck1)
    truck1.depart("Athens")
    print(truck1)
    truck1.arrive()
    print(truck1)
    cost = truck1.calculate_cost(210)
    print(f"Transport cost for 210 km: {cost:.2f}€")

    # --- Truck Test with Overload ---
    print("\n=== Truck Test with Overload ===")
    truck2 = Truck("ABG-1234", "Volvo FH", "Athens", 30)
    print(truck2.info())

    # --- Van Test ---
    print("\n=== Van Test ===")
    van1 = Van("MNO-7890", "Ford Transit", "Thessaloniki", 45)
    print(van1.info())
    print(van1)
    van1.depart("Larisa")
    print(van1)
    van1.arrive()
    print(van1)
    cost = van1.calculate_cost(150)
    print(f"Transport cost for 150 km: {cost:.2f}€")

    # --- Van Test with Package Overflow ---
    print("\n=== Van Test with Overflow ===")
    van2 = Van("XYZ-5555", "Mercedes Sprinter", "Heraklion", 120)
    print(van2.info())


if __name__ == '__main__':
    main()