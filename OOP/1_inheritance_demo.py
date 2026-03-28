class SchoolMember:
    """Represents any school member"""
    def __init__(self , name , age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember : {0}'.format(self.name))
        
    def tell(self):
        """Tell my details..."""
        print('Name: "{0}" , Age: "{1}" '.format(self.name , self.age), end=" ")
        

class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self, name, age , salary):
        SchoolMember.__init__(self , name, age) 
        self.salary = salary
        print('Initialized teacher : {0}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))
         
class Student(SchoolMember):
    """Represents a student"""
    def __init__(self, name, age , marks):
        SchoolMember.__init__(self , name, age) 
        self.marks = marks
        print('Initialized student : {0}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))
        
teacher = Teacher('Bob' , 50 , 2000)
student = Student('Alice' , 22 , 12)

print()

members = [teacher , student]

for member in members:
    member.tell()
    