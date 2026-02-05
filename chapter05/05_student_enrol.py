def enroll_students(*students , min_grade = 50 , department = "Computer Science" , **kwargs):
    
    print(f"Min grade : {min_grade}")
    print(f"Department : {department}")\
        
    print("\Enrolled Students:")
    for student in students:
        print(f" - {student}")
    
    
    print("Additional Information")
    for key , val in kwargs.items():
        print(f"{key} : {val}")



def main():
    
    
    pass
if __name__ == '__main__':
    main()