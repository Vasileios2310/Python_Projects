# lambda expressions
# Example: power of a number
# Parameters: 
# base (int) : the base number to be raised
# exp (int) : the exponent indication the power to which the based is raised
# Returns 
# The results of raising the 'base' to power of 'exp' 

def mypower(base , exp):
    return base ** exp

power_to = lambda base, exp: base ** exp
     
          
def main():
    print(mypower(2,2))
    print(power_to(2,2))
    
        
if __name__ == "__main__":
    main()        