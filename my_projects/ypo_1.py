import pickle
import os

class Student:
    def __init__(self , arithmos_mhtrwou , fullname , etos_eggrafis):
        """
        Αρχικοποιεί τα στοιχεία του φοιτητή,
        Αποθηκεύει ΑΜ, όνομα και έτος εγγραφής
        """
        self.arithmos_mhtrwou = arithmos_mhtrwou
        self.fullname = fullname
        self.etos_eggrafis = etos_eggrafis

    def __str__(self):
        """
        Επιστρέφει τα στοιχεία του φοιτητή σε αναγνώσιμη μορφή
        """
        return (
            f"ΑΜ : {self.arithmos_mhtrwou} , Όνομα : {self.fullname}, "
            f"Έτος εισαγωγής: {self.etos_eggrafis}")
    
class Course:
    """
    Αρχικοποιεί τους φοιτητές απο αρχείο pickle
    Επιστρέφει λίστα ή κενή λίστα σε περίπτωση σφάλματατος
    """
    def __init__(self , filename):
        """
        """
        self.filename = filename
        self.students = self.load_students()
        self.menu()

        
    def load_students(self):
        """
        """
        try:
            with open(self.filename , 'rb') as file:
                students = pickle.load(file)
                return students
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
        """
        """
        with open(self.filename, 'wb') as st:
            pickle.dump(self.students , st)
            st.close()


    def add_student(self):
        """
        """
        while True:
                try:
                    arithmos_mhtrwou = int(input("Εισάγετε ΑΜ φοιτητή:"))
                    if(arithmos_mhtrwou > 0):
                        break
                    else :
                        print('Ο αριθμός μητώου πρέπει να είναι μεγαλύτερος απο το μηδέν')
                except:
                    print('Εισαγωγή του ΑΜ εκ νέου (μεγαλύτερο απο μηδέν)')

        fullname = input("Εισάγετε ονοματεπώνυμο φοιτητή:")

        while True:
                try:
                    etos_eggrafis = int(input("Εισάγετε έτος εγγραφής:"))
                    if(etos_eggrafis >= 2000 and etos_eggrafis <= 2025):
                        break
                    else:
                        print('Ετος εισαγωγής θετκός ακέραιος μεταξύ 2000 - 2025')
                except:
                    print('Εισαγωγή του ετους εισαγωγής εκ νέου')
            
        my_student = Student(arithmos_mhtrwou , fullname , etos_eggrafis)
        self.students.append(my_student)

        print('Ο φοιτητής προστέθηκε με επιτυχία!')


    def display_students(self):
        """
        """
        if not self.students:
            print('Δεν βρέθηκαν φοιτητές')
        else:
            for student in self.students:
                print(student) 

    def menu(self):
        """
        """
        while True:
            print("\n=== Διαχείριση Φοιτητών ===")
            print("1. Προσθήκη φοιτητή")
            print("2. Εμφάνιση φοιτητών")
            print("3. Exit")

            choice = input("Επιλέξτε μια ενέργεια: ")
        
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.save_students()
                print("Exiting...")
                break
            else:
                print("Λάθος επιλογή, παρακαλώ επέλεξε ξανά.")

if __name__ == "__main__":
    Course("students.pkl")