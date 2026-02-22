def memorize(func):
    """A simple memorization to cache results of the function"""
    cache = {}
    
    def wrapper(n):
        if n in cache:
            print(f"Cache hit for Fibo({n})")
        else:
            print(f"Calculating Fibo({n})")
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memorize
def fibonacci(n):
    if n <=1 : return n
    else : return fibonacci(n-1) + fibonacci(n-2)

def main():
    print([fibonacci(n) for n in range(10)])
    
if __name__ == "__main__":
    main()   
        