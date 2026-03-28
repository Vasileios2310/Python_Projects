class Person:
    def __init__(self , name = '' , age = 0):
        self.name = name
        self.age = age
        
    def display(self):
        print('Person (%s , %d )' % (self.name , self.age))
        
    def __str__(self):
        return 'Person (%s , %d)' % (self.name , self.age)
        
    def __repr__(self):
        return str(self)
    
# my_person in STACK  ───────────────►  (Person instance στο HEAP)
# self  ───────────────►  (Person instance στο HEAP)
# [Person instance]
#  name ─────►  ''   (string object)
#  age  ─────►  0    (int object)

my_person = Person('Alice' , 10)
my_person1 = Person('Alice' , 10)
str(my_person)
print(my_person == my_person1)
my_person.display()

