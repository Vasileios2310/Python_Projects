def enroll_students(*students , min_grade = 50 , department = "Computer Science" , **kwargs):
    
    print(f"Min grade : {min_grade}")
    print(f"Department : {department}")
        
    print("Enrolled Students:")
    for student in students:
        print(f" - {student}")
    
    
    print("Additional Information")
    for key , val in kwargs.items():
        print(f"{key} : {val}")
        
    print('-----End of enrolement------')



def main():
    
    enroll_students("Alice" , "Bob")
    
    enroll_students("Bill" , "Helen" , "Sia" , academic_year = 2026 , semester = "Fall")
    
    enroll_students("Dalton" , min_grade=40 , department="Theater")
    
    enroll_students("John" , "Dave" , min_grade=70 , department="STEM" , academic_year = 2026 , semester = "Spring")
    
if __name__ == '__main__':
    main()