def is_square(legth , width):
    return legth == width

def main():
    try:
        length = int(input("Enter the length of the rectangular: "))
        width = int(input("Enter the width of the rectangular: "))
    except ValueError:
        print("Invalid input. Please give an integer")
        return
            
    if is_square(length , width):
        print("Rectangle is square")
    else:
        print("Rectangle is not square")

if __name__ == "__main__":
    main()