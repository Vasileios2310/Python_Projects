students = {
    'Alice':  [85 , 92 , 78],
    'Bill' : [97 , 95 , 88],
    'Charlie': [65, 82 , 80],
    'Diana' : [90 , 92 , 62],
    'Elina' : [98 , 97 , 100]
}



def main():
    #threshold
    
    threshold = int(input("Please insert a threshold :"))
    
    average_grades = {student : round(sum(grades) / len(grades) , 2) for student , grades in students.items()
                      if round(sum(grades) / len(grades) , 2) > threshold}
    
    print(average_grades)
    
    print('-' * 40)
    
    for student , grade in average_grades.items():
        print(f"{student} : {grade}")

if __name__ == '__main__':
    main()