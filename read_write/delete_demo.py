import os

if os.path.exists('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt'):
    os.remove('C:\\Users\\billk\\OneDrive\\Desktop\\test\\demo.txt')
else:
    print('the file does not exists')