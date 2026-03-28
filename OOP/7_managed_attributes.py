class Person:
    def __init__(self , fname):
        self.fname = fname
    
    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self , value):
        if not isinstance(value , str):
            raise TypeError('Expected a string')
        self._fname = value
    
    @fname.deleter
    def fname(self):
        raise AttributeError("Can't delete attribute")
    

p = Person('Bill')
print(p.fname)

p.fname = "Vas"
print(p.fname)

# can not insert a number 
#p.fname = 23
#print(p.fname)

# can not delete the attribute
#del p.fname
#print(p.fname)

