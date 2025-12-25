students = ("Alice" , "Bob" , "Charlie")

#Iterate
for Index , Value in enumerate(students):
    print(f"{Index} --> {Value}")
    
#Enhance for
for student in students:
    print(student , end="\n")
     
#first_student, second_student , third_student  = students[0] , students[1] , students[2]
#first_student, second_student , third_student  = students[0:3]
first_student, second_student , third_student = students


print(f"First student is {first_student}")
print(f"Second student is {second_student}")
print(f"Third student is {third_student}")

students = list(students)
students[0] = "Bill"
print(type(students))
students = tuple(students)
print(type(students))
print(students)