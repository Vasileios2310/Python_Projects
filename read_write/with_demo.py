with open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt', 'a') as f:
    f.write('Now the file has more content!')
    
    
with open('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt' ) as f:
    print(f.read())