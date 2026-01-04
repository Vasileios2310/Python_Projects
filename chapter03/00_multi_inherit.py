class Person:
    """
    Base class representing a Person.
    """
    def __init__(self , name : str , age : int):
        self.name = name
        self.age = age
        
    def display_info(self) -> None:
        print(f"Name : {self.name} , Age: {self.age}")

class Worker:
    """
    Class represanting a worker.
    """
    def __init__(self , job_title : str , company : str):
        self.job_title = job_title
        self.company = company
        
    def work(self) -> None:
        print(f"{self.job_title} working at {self.company}")    

class Student:
    """
    Class representing a student
    """
    def __init__(self , major : str , university : str):
        self.major = major
        self.university = university
        
    def study(self) -> None:
        print(f"Studing {self.major} at {self.university}")
        
class WorkingStudent(Person , Worker , Student):
    """
    Derived class representing a Person who is both Worker and Student
    """
    
    def __init__(self, name:str, age:int , job_title:str , company:str , major:str , university:str):
        Person.__init__(self , name , age)
        Worker.__init__(self , job_title , company)
        Student.__init__(self , major , university)

def main() -> None:
    #create a working student object
    ws = WorkingStudent(
        name="Alice",
        age = 25,
        job_title="Software Engineer",
        company="TechCrop",
        major = "AI Manager",
        university="MIT"
    )
    
    ws.display_info()
    ws.work()
    ws.study()

if __name__ == "__main__":
    main()