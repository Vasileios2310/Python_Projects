def cheesehop(kind , *arguments , **keywords):
    print("-- Do you have any " , kind , "?")
    print("-- I am sorry , we are all out of " , kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":" , keywords[kw])
  
print("one parameter")      
cheesehop("Limburger")

print("three parameters")      
cheesehop("Limburger", "It's very runny, sir.","It's really very, VERY runny, sir.")

print("ALL parameters")  
cheesehop("Limburger", "It's very runny, sir.","It's really very, VERY runny, sir."
          ,shopkeeper="Michael Palin",client="John Cleese",sketch="Cheese Shop Sketch")