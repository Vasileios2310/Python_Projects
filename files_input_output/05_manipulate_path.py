import os

path = 'C:\\Users\\billk\\OneDrive\\Desktop\\test.txt'

print(os.path.basename(path))

print(os.path.dirname(path))

print(os.path.join('tmp' , 'data' , os.path.basename(path)))