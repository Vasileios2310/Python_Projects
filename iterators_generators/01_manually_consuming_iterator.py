with open('password.txt') as f:
    try:
        while(True):
            line = next(f)
            print(line , end = '')
    except StopIteration :
        pass