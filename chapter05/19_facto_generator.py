def facto():
    n , result = 0 , 1
    while True:
        yield result    # stops yield
        n += 1          # continue the next()
        result *= n
     

def main():
    # create a generator object for factorials
    fac = facto()
    
    # factoria 0 - 9 , next() gives the next value until found yield
    for i in range(10):
        print(f"{i}! = {next(fac)}")
     
    print(next(fac)) # it gives 10!

if __name__ == '__main__':
    main()