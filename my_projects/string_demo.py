s = "Artificial Intelligence with Python by Prateek Joshi"
s1 = s[0:5]
#print(s1)

s2 = s[-9:]
#print(s2)

#Atfca nelgnewt yhnb rte oh
s3 = s[::2]
#print(s3)

#'ishoJ keetarP yb nohtyP htiw ecnegilletnI laicifitrA'
s3 = s[-1::-1]
#print(s3)

#' tleei '
s4 = s[10] + s[2] + s[9] + s[14] + s[19] + s[25] + s[10] 
#print(s4) 

#'th Python by Prateek Joshi'
s5 = s[26:]
#print(s5)

#'icial Intelligence with Python by Prateek'
s6 = s[5:46]
#print(s6)




ai_books = {
    "Artificial Intelligence with Python by Prateek Joshi",
    "Artificial Intelligence Programming with Python: From Zero to Hero by Perry Xiao",
    "Python Machine Learning by Sebastian Raschka",
    "Hands-On Artificial Intelligence with Java for Beginners by Nisheeth Joshi",
    "ChatGPT for Java: A Hands-on Developer's Guide to ChatGPT and Open AI APIs by Bruce Hopkins",
    "Java Artificial Intelligence and Deep Learning by Sage Rylan"
}

java_books = {
    "Hands-On Artificial Intelligence with Java for Beginners by Nisheeth Joshi",
    "ChatGPT for Java: A Hands-on Developer's Guide to ChatGPT and Open AI APIs by Bruce Hopkins",
    "Java Artificial Intelligence and Deep Learning by Sage Rylan",
    "Big Java: Early Objects 7th Edition by Cay S. Horstmann",
    "Effective Java by Joshua Bloch"
}

python_books = {
    "Artificial Intelligence with Python by Prateek Joshi",
    "Artificial Intelligence Programming with Python: From Zero to Hero by Perry Xiao",
    "Python Machine Learning by Sebastian Raschka",
    "A Byte of Python by Swaroop C H.",
    "Python Crash Course by Eric Matthes"
}

print("------------1----------")
# Έκφραση που επιστρέφει σύνολο από όλα τα βιβλία της Python που δεν έχουν ως θέμα την τεχνητή νοημοσύνη.
str_python = 'Artificial Intelligence'
python_books_without_AI = set()
for item in python_books:
    if str_python not in item:
        python_books_without_AI.add(item)
print(python_books_without_AI)

print("------------2----------")  
# Έκφραση που επιστρέφει σύνολο από όλα τα βιβλία της  Java που έχουν ως θέμα την τεχνητή νοημοσύνη. 
str_java = 'Artificial Intelligence'
java_books_with_AI = set()
for item in java_books:
    if str_java in item:
        java_books_with_AI.add(item)
print(java_books_with_AI)

print("------------3----------")
# Έκφραση που επιστρέφει σύνολο από όλα τα βιβλία της βιβλιοθήκης που δεν αφορούν την τεχνητή νοημοσύνη.
str_out = 'Artificial Intelligence'
books_without_AI = python_books.union(ai_books).union(java_books)
lib_books_without_AI = set()
for item in books_without_AI:
    if str_out not in item:
        lib_books_without_AI.add(item)
print(lib_books_without_AI)


print("------------4----------")
# Έκφραση που επιστρέφει σύνολο από όλα τα βιβλία της βιβλιοθήκης που είναι είτε για τεχνητή νοημοσύνη είτε για Python αλλά όχι και τα δύο
str_out = 'Artificial Intelligence'
books_union = python_books.union(ai_books)
lib_books_with_AI_or_Python = set()
for item in books_union:
    if str_out not in item:
        lib_books_with_AI_or_Python.add(item)
print(lib_books_with_AI_or_Python)


print("------------5----------")
# Έστω book μια συμβολοσειρά που περιέχει το όνομα του βιβλίου και του συγγραφέα όπως στα παραδείγματα που προηγήθηκαν
# (π.χ. "Python Crash Course by Eric Matthes").
# Γράψτε την έκφραση, στην book[έκφραση],  που απομονώνει το όνομα του συγγραφέα (π.χ. "Eric Matthes") από τη συμβολοσειρά. 
# Υπόδειξη: κάνετε χρήση της συνάρτησης find με το κατάλληλο όρισμα και δημιουργήστε μία έκφραση που να την περιέχει,
# ώστε να απομονώσετε το όνομα του συγγραφέα για κάθε πιθανή συμβολοσειρά που δόθηκε.

java_books_with_AI = set()
for item in java_books:
    index = item.find("by")
    str_name = item[index:]
    print(str_name)