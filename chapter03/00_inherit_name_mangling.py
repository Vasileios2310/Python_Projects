#name mangling
class Base:
    def __init__(self):
        self.__private = "I am private"
        self._protected = "I am protected"
        self.public = "I am public"
        
    def __private_method(self):
        return "I am private method"
    
    # returns attribute private
    def get_private(self):
        return self.__private
    
    # returns method private
    def call_private_method(self):
        return self.__private_method()

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__private = "I am private from derived class"
        
    def get_derived_private(self):
        return self.__private

def main():
    base = Base()
    print(base.public)
    print(base._protected)
    # Python rename the attribute like this 
    #print(base._Base__private)
    #print(base.__private)
    print(base.get_private())
    #print(base.__private_method)
    print(base.call_private_method())
    print("derived object")
    derived = Derived()
    print(derived.public)
    print(derived._protected)
    #print(derived.__private_method)
    #print(derived.__private)
    print("Name mangling")
    print(derived._Derived__private)
    print(derived.get_private())

if __name__ == "__main__":
    main()    