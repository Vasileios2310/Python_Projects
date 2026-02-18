def upscale_grades(students_grades):
    return {name : (grade + 1 if grade <= 9 else grade) for name , grade in students_grades.items()}



def filter_passed_grades(students_grades):
    return {name : grade for name , grade in students_grades.items() if grade >= 5}
    
def categorized_grades(students_grades):  
      passed = {name : grade for name , grade in students_grades.items() if 5 <= grade < 10 }
      failed = {name : grade for name , grade in students_grades.items() if grade < 5 }
      honors = {name : grade for name , grade in students_grades.items() if grade == 10 }
      
      return passed , failed , honors
  
def calculate_average(students_grades):
    if students_grades:
        return round_average(sum(students_grades.values()) / len(students_grades))
    return 0

def round_average(average_grade):
    return round(average_grade)

def main():
    students_grades = {
                        "Maria": 4,
                        "Nikos": 7,
                        "Elina": 10,
                        "Giorgos": 6,
                        "Katerina": 8,
                        "Dimitris": 5,
                        "Bill": 10,
                        "Panagiotis": 4,
                        "Ioanna": 2,
                        "Kostas": 7
}
    
    print("Original students grades : " , students_grades)
    print(upscale_grades(students_grades))
    
    print("Passed grades: " ,filter_passed_grades(students_grades))
    print('-' * 30)
    passed , failed , honors = categorized_grades(students_grades)
    print("\nPassed")
    for name , grade in passed.items():
        print(f"{name}:{grade}")
    print('-' * 30)  
    print("\nFailed")
    for name , grade in failed.items():
        print(f"{name}:{grade}") 
    print('-' * 30) 
    print("\nHonors")
    for name , grade in honors.items():
        print(f"{name}:{grade}")
    
    print('-' * 30)
    print("Failed grades: " , failed)
    print("Honors grades: " , honors)
    print('-' * 30)
    print("Averagae" , calculate_average(students_grades))
    
if __name__ == '__main__':
    main()