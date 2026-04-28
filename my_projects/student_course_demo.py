import pickle
import os

class Student:
        def __init__(self, student_id, fullname, enrollment_year):
            self.student_id = student_id
            self.fullname = fullname
            self.enrollment_year = enrollment_year

        def __str__(self):
            return (
            f"ID: {self.student_id}, Name: {self.fullname}, "
            f"Enrollment Year: {self.enrollment_year}")

class Course:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_students()
        self.menu()

def load_students(self):
    try:
        with open(self.filename, 'rb') as file:
            self.students = pickle.load(file)
            return self.students
    except FileNotFoundError:
        print(f"File not found: {self.filename}")
        return []
    except pickle.UnpicklingError:
        print("Error: The file content is not a valid pickle format.")
        return []
    except EOFError:
        print("Error: The file is incomplete or corrupted.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def save_students(self):
    with open(self.filename, 'wb') as st:
        pickle.dump(self.students, st)

def add_student(self):
    while True:
        try:
            student_id = int(input("Enter student ID: "))
            if student_id > 0:
                break
            else:
                print("Student ID must be a positive number.")
        except:
            print("Invalid input. Please enter a valid positive number.")

    fullname = input("Enter full name: ")

    while True:
        try:
            enrollment_year = int(input("Enter enrollment year: "))
            if 2000 <= enrollment_year <= 2025:
                break
            else:
                print("Enrollment year must be between 2000 and 2025.")
        except:
            print("Invalid input. Please enter a valid year.")

    student = Student(student_id, fullname, enrollment_year)
    self.students.append(student)

    print("Student added successfully!")

def display_students(self):
    for student in self.students:
        print(student)

def menu(self):
    while True:
        print("\n=== Student Management ===")
        print("1. Add student")
        print("2. Display students")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            self.add_student()
        elif choice == '2':
            self.display_students()
        elif choice == '3':
            self.save_students()
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    Course("students.pkl")
