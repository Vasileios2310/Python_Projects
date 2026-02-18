def fibo():
    a , b = 0 , 1
    while True:
        yield a                  # stops yield
        a , b = b , a + b        # continue the next()
        
     

def main():
    # create a generator object for factorials
    fib = fibo()
    
    for i in range(10):
        print(f"Fib ({i}) = {next(fib)}")
     
    new_fibo = fibo()
    fibo_list_15 = [next(new_fibo) for a in range(16) ]
    print(fibo_list_15)

if __name__ == '__main__':
    main()