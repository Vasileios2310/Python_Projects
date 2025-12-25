class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        
def where_is(point):
    match point:
        case Point(x=0 , y=0):
            print('origin')
        case Point(x=0, y=y):
            print(f"y={y}")
        case Point(x=x, y=0):
            print(f"x={x}")
        case Point(x=x , y=y):
            print(f"x={x} , y={y}")
        case _:
            print("not a point")
    
p1 = Point(5,8)       
where_is(p1)