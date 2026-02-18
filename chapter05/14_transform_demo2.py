def upscale_grades(grades):
    """
    Upscale grade by 1 if grade <= 9
    """
    upscaled = [grade + 1 if grade <= 9 else grade for grade in grades]
    return upscaled

def filter_pass(grades):
    """
    Filter grades (grade >= 9)
    """
    
    passed = [grade for grade in grades if grade >= 5]
    return passed

def categorized_grades(grades):
    """Categorize grades into:
        - passed (grade >= 5 and grade <= 10)
        - failed (grade < 5)
        - honors (grade == 10)
    """
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    
    return passed , failed , honors

def calculate_average(grades):
    average_grade = sum(grades) / len(grades)
    
    return sum(grades) / len(grades) if grades else 0
    
def main():
    grades = [1,2,3,4,5,6,7,8,9]
    
    upscaled_grades = upscale_grades(grades)
    print("Original grades: " , grades)
    print("Upscaled grades: " , upscaled_grades)
    
    passed_grades = filter_pass(upscaled_grades)
    print("Passed grades: " , passed_grades)
    
    passed , failed , honors = categorized_grades(upscaled_grades)
    print("Passed grades: " , passed)
    print("Failed grades: " , failed)
    print("Honors grades: " , honors)
    
if __name__ == '__main__':
    main()