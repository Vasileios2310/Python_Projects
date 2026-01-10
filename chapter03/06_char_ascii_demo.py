def process_characters():
    ch = input("Please insert a character: ")
    
    while ch != "#":
        print(ch , ":" , ord(ch))
        ch = input("Please insert a character: ")
    
    print("Good bye")
    
def process_characters_break():
    while True:
        ch = input("Please insert a character: ")
        if ch == "#":
            break
        print(ch , ":" , ord(ch))
    
    print("Good bye with break")
    
    
def main():
    process_characters()
    
    process_characters_break()
    
    
    
    
if __name__ == "__main__":
    main()