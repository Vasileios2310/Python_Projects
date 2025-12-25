class Point():
    
    __count = 0
    def __init__(self , x = 0, y = 0):
        self._x = x
        self._y = y
        Point.__count += 1
        
    def __str__(self):
        return f"({self._x} {self._y})"
    
    def __repr__(self):
        return f"Point(x = {self._x} , y {self._y})"
    
    def __eq__(self, value):
        if isinstance(value , Point):
            return self._x == value._x and self._y == value._y
        else:
            return False
        
    def __lt__(self, value):
        if isinstance(value , Point):
            return self._x < value._x and self._y < value._y
        else:
            return False
      
    @classmethod  
    def get_count(cls):
        return cls.__count 
    
    #properties
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self , x):
        self._x = x
    
    #properties
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self , y):
        self._y = y
        

def main():
    p1 = Point(10, 20)
    p2 = Point()
    #print(Point.get_count())
    
    p2.x = 10
    p2.y = 20
    
    print(p1)
    print(p2)
    print(p1 == p2)
    
    print(repr(p1))
    
    print(p1 < p2)
    
if __name__ == "__main__":
    main()