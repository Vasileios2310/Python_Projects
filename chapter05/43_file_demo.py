import os 

def read_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error : File {file_path} does not exist or it is not  valid")
        return
    
    try:
        with open(file_path , 'r') as f:
            print("Some metadata")
            print("Filename" , f.name)
            print("Closed" , f.closed)
            print("Opening Mode" , f.mode)
            
            print("file contents")
            contents = f.read()
            print("contents :" , contents)
            
    except FileNotFoundError:
        print("Error : {file_path} not found")
    except IOError as ex:
        print("Error reading file '{file_path}':  {ex}")
        
    print("File close after with-block" , f.closed)
    
def create_file(file_path , content):
    try:
        with open(file_path , 'w') as f:
            f.write(content)
            print(f"File {file_path} created with content: {content}")
    except IOError as ex:
        print(f"Creating file '{file_path}' : {ex}")
        
def update_file(file_path , content):
    if not os.path.isfile(file_path):
        print(f"Error : File {file_path} does not exist or it is not  valid")
        return
    
    try:
        with open(file_path , 'a') as f:
            f.write(content)
            print(f"File {file_path} updated with content: {content}")
    except IOError as ex:
        print(f"Error : Updating file '{file_path}' : {ex}")
        
def delete_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error : File {file_path} does not exist or it is not  valid")
        return
    
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully")
    except IOError as ex:
        print(f"Error deleting file '{file_path}' : {ex}")
                 
def main():
    print("create a file")
    create_file('test.txt' , "This is my first text")
    
    read_file('test.txt')
    
    update_file('test.txt' , "This is my second text")
    
    delete_file('test.txt')
    
    read_file('test.txt')
    

if __name__ == '__main__':
    main()