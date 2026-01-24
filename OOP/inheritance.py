class UniversityMember():
    def __init__(self,  name , age):
        self.name = name
        self.age = age
        print('Initializing University member: ' , self.name)
    def display(self):
        print('Name: "{0}" Age: "{1}"'.format(self.name , self.age) , end='')

class Professor(UniversityMember):
    def __init__(self, name, age,salary):
        UniversityMember.__init__(self, name, age)
        self.salary = salary
        print('Initializing teacher: ' , self.name)
    def display(self):
        UniversityMember.display(self)
        print('Salary:  ' , self.salary)

class Student(UniversityMember):
    def __init__(self, name, age , TaxNo):
        UniversityMember.__init__(self , name, age)
        self.TaxNo = TaxNo
        print('Initializing student' , self.name)
    def display(self):
        UniversityMember.display(self)
        print('Tax Number: ', self.TaxNo)
        
        
professor = Professor('Alice' , 35 , 1500)
professor.display()

student = Student('Bob' , 20 , 123456789)
student.display()
