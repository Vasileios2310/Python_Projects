class Base:
    def __init__(self , name):
        self.name = name
    
    
class Derived(Base):
    def __init__(self , name , y):
        super().__init__(name)
        self.y = y
        
def main():
    base = Base('b')
    der = Derived('a' , 'D')
    
    print(der.name , der.y)

if __name__ == "__main__":
    main()