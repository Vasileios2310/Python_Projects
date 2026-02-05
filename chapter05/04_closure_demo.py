def department_id_generator(department):
    last_id = 0
    
    def generate_id():
        nonlocal last_id
        last_id += 1
        return f"{department} --> {last_id}"
       
    return generate_id
    

def main():
    python_id_gen = department_id_generator("python")
    android_id_gen = department_id_generator("android")
    
    print(python_id_gen())
    print(android_id_gen())
    print(python_id_gen())
    print(android_id_gen())
    
    
if __name__ == '__main__':
    main()