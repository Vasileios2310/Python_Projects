# The Collatz sequence, also called the 3n + 1 problem, is the simplest impossible math problem.
# 1. If n is even, the next number n is n / 2.
# 2. If n is odd, the next number n is n * 3 + 1.
# 3. If n is 1, stop. Otherwise, repeat.

import sys
import time

print('Collatz Sequence, or, the 3n + 1 Problem')

print('Enter a starting number - grater than 0 or Quit')
num = input('>>>')


if not num.isdecimal() or num == '0':
    print('You must enter a number greater than 0')
    sys.exit()
    
choice = int(num)
print(choice , end='' , flush=True) 
while choice != 1:
    if choice % 2 == 0:
        choice = choice / 2
    else:
        choice = choice * 3 + 1
        
    print(', '  + str(choice), end='' , flush=True)
    time.sleep(0.1)
print()