def age_read():
    while True:
        try:
            age = int(input('Give your age as integer: '))
            return age
        except ValueError:
            print('The age must be in integer format')
            
            
my_age = age_read()
print(my_age)