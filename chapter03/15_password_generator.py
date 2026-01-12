import random
import string

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    """
    Generates a random password on the user specific length.
    """
    try:
        password_length = int(input("Please give the password length: "))
        
        if password_length <= 0:
            print("Password length must be greater than zero")
            raise ValueError
    except ValueError:
        print("Invalid input, please give a valid number")
        return
    
    random.shuffle(characters)
    password = []
    
    for i in range(password_length):
        password.append(random.choice(characters))
            
    # double shuffle the generated password []
    random.shuffle(password)
    
    # now i want to convert the password from list to string
    string_password = "".join(password)
    
    print(f"\nGenerated password : {string_password}")
        
def main():
    while True:
        option = input("\nDo you want to create the password? ('y' for yes or 'q' for quit): ")
        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'q':
            print("Goodbye")
            break
        else:
            print("Wrong input")


if __name__ == "__main__":
    main()