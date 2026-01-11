# ΠΡΟΓΡΑΜΜΑ: ΣΥΣΤΗΜΑ ΔΙΑΧΕΙΡΙΣΗΣ ΒΙΒΛΙΟΘΗΚΗΣ
import statistics
import copy

def display_menu():
    print("\n=== ΣΥΣΤΗΜΑ ΒΙΒΛΙΟΘΗΚΗΣ ===")
    print("1. Εμφάνιση βιβλίων")
    print("2. Νέος δανεισμός")
    print("3. Επιστροφή βιβλίου")
    print("4. Στατιστικά βαθμολογίας")
    print("5. Έξοδος")

# Λεξικό βιβλιοθήκης
# Κάθε βιβλίο έχει ως "κλειδί" το ISBN του.
# Η τιμή κάθε κλειδιού είναι ένα δεύτερο λεξικό με τα στοιχεία του βιβλίου.
Library = {
    '9789604618020': {'titlos': 'Ιλιάδα', 'syggrafeas': 'Όμηρος', 'diathesimo': True},
    '9789604619126': {'titlos': '1984', 'syggrafeas': 'Όργουελ', 'diathesimo': True},
    '9789604617153': {'titlos': 'Ο Πρίγκιπας', 'syggrafeas': 'Μακιαβέλι', 'diathesimo': True},
    '9789604618884': {'titlos': 'Η Δημοκρατία', 'syggrafeas': 'Πλάτωνας', 'diathesimo': True}
}

# Λίστα με τα ονόματα των δανειζομένων
daneizomenoi = ['Πετρίδου Μαρία', 'Δημόκα Μαρία', 'Κοσμίδης Γεώργιος']

# Λεξικό που περιέχει τις βαθμολογίες που έχει λάβει κάθε βιβλίο
vathmologies = {
    '9789604618020': [4, 5, 4],
    '9789604619126': [5, 4, 5, 4],
    '9789604617153': [3, 4, 4],
    '9789604618884': [4, 3, 4, 4]
}

# Βήμα 1:Εμφάνιση των βιβλίων του λεξικού βιβλιοθήκης
def display_books():
    print('ISBN | ΤΙΤΛΟΣ - ΣΥΓΓΡΑΦΕΑΣ | ΔΙΑΘΕΣΙΜΟΤΗΤΑ')
    for isbn, obj in Library.items():
        diath = 'ΔΙΑΘΕΣΙΜΟ' if obj['diathesimo'] else 'ΔΑΝΕΙΣΜΕΝΟ'
        print(f"{isbn} | {obj['titlos']} - {obj['syggrafeas']} | {diath}")
        
    
# Βήμα 2: ΝΕΟΣ ΔΑΝΕΙΣΜΟΣ (με βάση το ISBN με έλεγχο)
def add_new_loan():
    isbn_to_loan = input("Παρακαλώ εισάγετε το επιθυμητό ISBN ").strip()
    full_name = input("Παρακαλώ εισάγετε τον ονοματεπώνυμο σας ").strip()
    
    found = False
    
    for x , obj in Library.items():
        if isbn_to_loan == x:
            found = True
            
            if obj['diathesimo'] == False:
                print('Το βιλίο είναι ηδη δανεισμένο')
                return
            
            if full_name not in daneizomenoi:
                daneizomenoi.append(full_name)
                print("Προσθήκη νέου δανειζόμενου" , full_name)
            
            obj['diathesimo'] = False
            
            print(f"Επιτυχής δανεισμός για το βιβλίο {obj['titlos']}")
            return
        
    if not found:
        print('Το ISBN δεν υπάρχει στη βιβλιοθήκη') 
        
    
# Βήμα 3: ΕΠΙΣΤΡΟΦΗ ΒΙΒΛΙΟΥ (με βάση το ISBN με έλεγχο)
# -------------------------------
def return_book():
   isbn_to_return = input("Παρακαλώ εισάγετε το ISBN του βιβλίου προς επιστροφή ").strip()
   
   book_exist = False
   
   for x , obj in Library.items():
       if isbn_to_return == x:
           book_exist = True
           
           if obj['diathesimo'] == True:
                print('Το βιβλίο είναι ηδη διαθέσιμο, αρα δεν μπορεί να επιστραφεί ')
                return
            
           obj['diathesimo'] = True
           
           while True:
               try:
                   rate = int(input('Βαθμολογία για το βιβλίο (1 εως 5) '))
                   
                   if 1 <= rate <= 5:
                       break
                   else:
                       print('Δώσε αριθμό απο 1 εως 5')  
                       
               except ValueError: print('Δώσε αριθμό απο 1 εως 5')
            
           if isbn_to_return not in vathmologies:
               vathmologies[isbn_to_return] = []
           vathmologies[isbn_to_return].append(rate)
            
           print(f"Επιτυχής επιστροφή! Το βιβλίο «{obj['titlos']}» βαθμολογήθηκε με {rate}.")
           return
                
   if not book_exist:
        print('Το ISBN δεν υπάρχει στη βιβλιοθήκη') 
               

# Βήμα 4: ΣΤΑΤΙΣΤΙΚΑ ΒΑΘΜΟΛΟΓΙΑΣ (Εύρεση και εμφάνιση ΜΟ Βαθμολογιας κάθε βιβλίου
#                                 με 1 δεκαδικό ψηφίο και πλήθους αξιολογήσεων)
# -------------------------------
def display_rating_statistics():
    
    library_copy = copy.deepcopy(Library)
    
    for isbn , element in library_copy.items():
        ratings = vathmologies.get(isbn , [])
        count = len(ratings)
        
        element.pop('diathesimo' , None)
        
        element['Average'] = round(statistics.mean(ratings) , 1) if count else None
        element['amount ratings'] = count
                
    for isbn, element in library_copy.items():
        avg = element['Average']
        avg_str = f"{avg:.1f}" if avg is not None else "—"
        count = element['amount ratings']

        print(f"{isbn} | {element['titlos']} | {element['syggrafeas']} | {avg_str} (απο {count} αξιολογήσεις)")

# -------------------------------

print("=== ΣΥΣΤΗΜΑ ΔΙΑΧΕΙΡΙΣΗΣ ΒΙΒΛΙΟΘΗΚΗΣ ===")

while True:
    display_menu()
    epilogi = input("Επιλογή (1-5): ")

    if epilogi == "1":
        display_books()
    elif epilogi == "2":
        add_new_loan()
    elif epilogi == "3":
        return_book()
    elif epilogi == "4":
        display_rating_statistics()
    elif epilogi == "5":
        print("Τέλος προγράμματος.")
        break
    else:
        print("Μη έγκυρη επιλογή, προσπαθήστε ξανά.")

