class Point:
    def __init__(self , x , y):
        #self.x = x --> completely public
        #self.y = y --> completely public
        #self._x = x --> Protected
        #self._y = y --> Protected
        self.__x = x # --> name mangling - private 
        self.__y = y # --> name mangling - private  --> real access p._Point__x
        
    def __str__(self):
        return f"({self.__x} , {self.__y})"
    
    def __add__(self, other):
        if isinstance(other , Point):
            return Point(self.__x + other.__x , self.__y + other.__y)
        elif isinstance(other , (int , float)):
            return Point(self.__x + other , self.__y + other)
        else:
            raise TypeError(f"Unsupported types")
        
    def __radd__(self, other):
        return self.__add__(other)
        
    def __eq__(self, other):
        if isinstance(other , Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self , value):
        self.__x = value
        
    @property
    def y (self):
        return self.__y 
    
    @y.setter
    def y (self , value):
        self.__y = value
        
        
def main():
    p1 = Point(1, 2)
    p2 = Point(2,4)
    
    print("p1 + p2 = " , p1 + p2)  ## + Python is hunting for __add__  and happens p1.__add__(p2)
    print("p1 + 10" , p1 + 10)
    print("p1 == Point(1,2)" , p1 == Point(1,2)) 
    print("p1 == 'Hello' : " , p1 == 'Hello')

    print("p1.x = " , p1.x)
    p1.x = 100
    print(p1)
    
    print("10 + p1 = " , 10 + p1 ) # + Python is hunting for __radd__  and happens p1.__add__(p2)
  
if __name__ == '__main__':
    main()