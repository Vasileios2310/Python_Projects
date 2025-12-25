students = ("Alice" , "Bob" , "Charlie")
print(students)

#students = tuple(["Bill"] + list(students))
#print(students)

students = tuple(["Bill"] + list(students)[1:])
print(students)

for index , value in enumerate(students , start= 100):
    print(f"Index : {index} --> Value : {value}")
