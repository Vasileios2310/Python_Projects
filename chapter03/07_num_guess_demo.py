import random

def get_user_guess():
    while True:
        try:
            return int(input("Please give a number"))
        except ValueError:
            print("Invalid input")
            
def check_guess(secret , guess):
    if (secret == guess):
        print("Bingo!! Secret number is : ", secret)
        return True
    elif abs(guess - secret) <= 5:
        print("Hot")
    else:
        print("Cold")
        return False
        
def main():
    secret_number = random.randint(1,10)
    MAX_TRIES = 5
    tries = 0
    
    while tries < MAX_TRIES:
        guess = get_user_guess()
        if check_guess(secret_number , guess):
            break
        tries += 1
    
    if tries == MAX_TRIES:
        print("Ypu reached the number of max tries" , MAX_TRIES)
        
    
if __name__ == "__main__":
    main()