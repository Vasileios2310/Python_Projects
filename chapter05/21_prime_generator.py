def is_prime(n):
    """ Checks if a number is prime or not"""
    if n < 2:
        return False
    for i in range(2 , int(n ** 0.5) + 1):
        if n % i == 0:
            return True
        return False

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def main():
    # create a generator object for factorials
    prime = prime_generator()
    
    for _ in range(25):
        print(next(prime))

if __name__ == '__main__':
    main()        