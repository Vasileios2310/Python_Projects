class Pair:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Pair({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'({self.x!s} , {self.y!s})'
    


p = Pair(3,5)
print('p is {0!r}'.format(p))
print('p is {0!s}'.format(p))
