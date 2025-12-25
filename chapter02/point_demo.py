import math

class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x} , {self.y})"
        
    def distance(self , point):
        return math.sqrt(math.pow(self.x - point.x , 2) + math.pow(self.y - point.y , 2))    
        
def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    
    print(p1.distance(p2))
    
    p1.x = 15
    p2.y = 15
    print(p1.distance(p2))
    
    print(f"Point p1 : {p1}")
    
    
if __name__ == "__main__":
    main()