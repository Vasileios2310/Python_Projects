import os

if not os.path.exists('somefile'):
    with open('somefile' , 'wt' ) as f:
        f.write('Hello World\n')
else:
    print('file already exists')