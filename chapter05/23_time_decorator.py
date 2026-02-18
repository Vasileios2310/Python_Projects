import time

def timer_decorator(func):
    def inner_function(*args , **kwargs):
        start_time = time.perf_counter()
        
        result = func(*args , **kwargs)
        
        end_time = time.perf_counter()
        
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    
    return inner_function


def sum_func(n):
    return sum(range(n))

# decorate manually sum 
sum_func = timer_decorator(sum_func)
print(sum_func(1_000_000))

@timer_decorator
def average_func(n):
    if n == 0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n

print(average_func(100))

@timer_decorator
def reverse_string(s):
    return "".join(reversed(s))

print(reverse_string("HELLO WORLD!!!"))