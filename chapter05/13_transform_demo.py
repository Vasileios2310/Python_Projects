def main():
    grades = [7 , 5 , 9 , 10 , 3]
    
    # increase all grades by 1
    upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades  ]
    print("Upscaled grades : " , upscaled_grades)
    
    
    # increase all grades by 1 (using map function)
    upscaled_grades2 = list(map(lambda grade : grade + 1 if grade <= 9 else grade , grades))
    print("Upscaled grades 2 : " , upscaled_grades2)
    
    
    passed_grades = [grade for grade in grades if grade >= 5]
    print(passed_grades)
    
    passed_grades2 = list(filter(lambda grade : grade >=5 , grades))
    print(passed_grades2) 
    
    # filtering all grades >= 5 (using filter function)
    passed_grades = list(map(lambda grade : grade + 1 if grade <= 9 else grade , filter(lambda grade : grade >= 5 , grades)))
    print(passed_grades)
    
    
if __name__ == "__main__":
    main()