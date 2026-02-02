def calculate_grade(assignments_score , mid_score , final_score):
    def weighted_score():
        assignment_score = sum(assignments_score) / len(assignments_score)
        return assignment_score * 0.4 + mid_score * 0.3 + final_score * 0.3


    def determine_grade(average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 65:
            return 'C'
        else : 
            return 'D'
        
    average = weighted_score()
    grade = determine_grade(average)
    
    return average , grade

def main():
    # list_of_grades = [[85 , 90 , 88 , 92] , 92 , 95]
    
    final_average , final_grade = calculate_grade([85 , 90 , 88 , 92] , 92 , 95)
    
    print(f"Final average: {final_average:.2f}")
    print(f"Final grade: {final_grade}")


if __name__ == '__main__':
    main()