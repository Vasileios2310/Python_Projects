class Student:
     def __init__(self , firstname , lastname):
         self.firstname = firstname
         self.lastname = lastname
         

def main():
    st = Student(firstname="Bob" , lastname="M.")
    
    print("Firstname is :" , st.firstname)
    print("Lastname is :" , st.lastname)
    
    st.hello_world = "Hello World"
    
    print(st.hello_world)

if __name__ == "__main__":
    main()
    
    