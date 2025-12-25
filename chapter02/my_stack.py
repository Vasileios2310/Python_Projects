import re

stack = []
num = 0

def push(list , item):
    list.append(item)
    
def pop(list):
    if list:
        list.pop()
    else:
        print('List is empty')
        
def print_list(list):
    if list:
        print('Current stack : ' , list)
    else:
        print("Stack is empty")
        
def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. Print stack")
    print("4. Q/q for quit")
    
def get_choice():
    return input("Please provide a choice\n")


def main():
    choice = 0
    num = 0
    out_num = 0
    
    while True:
        print_menu()
        choice = get_choice()
        
        if not choice:
            continue
        
        if choice == 'Q' or choice == 'q':
            break
        
        pattern = r"^\d$" #integer (0 - 9)
        valid = re.match(pattern, choice)
        
        if not valid:
            print("Please insert choice 1 - 4")
            continue
        
        choice = int(choice)
        
        match choice:
            case 1:
                num = input("Please insert a number: ")
                pattern = r"^\d+$"
                valid = re.match(pattern , num)
                
                if not valid:
                    print("Error")
                    continue
                 
                num = int(num)
                push(stack , num)
                print(str(num) + "inserted")   
            case 2:
                out_num = pop(stack)
                if out_num is not None:
                    print("You got" , out_num)
            case 3:
                print_list(stack)
            case _:
                print("Not valid choice")
                
        
if __name__ == "__main__":
    main()