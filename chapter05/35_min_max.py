def main():
    
    students = {
    'Alice':   [ 85 ],
    'Bill' :   [ 97 ],
    'Charlie': [ 55 ],
    'Diana' :  [ 90 ],
    'Elina' :  [ 98 ]
    }
    
    # the lowest grade in the dictionary for each student  
    students_lowest_grade = { student : min(grade) for student , grade in students.items() }   #--> the lowest grade in the dictionary for each student
    
    student_with_lowest_grade = min(students , key= students.get) 
    print("Students with lowedst grade : " , student_with_lowest_grade)
    
    print("For each Student lowedst grade : " , students_lowest_grade)
    
    # find the student with smallest name alpabetically
    student_with_smallest_name = min(students)
    print("student with smallest name" , student_with_smallest_name)

     # find the student with shortest name by length
    student_with_shortest_name_length = min(students , key=len)
    print("student with shortest name" , student_with_shortest_name_length)


if __name__ == '__main__':
    main()