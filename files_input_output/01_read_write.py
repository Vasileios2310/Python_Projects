# read the entire file as a sigle string
with open('test.txt' , 'rt') as f:
    data = f.read()
    
print(data)

with open('test.txt' , 'wt') as f:
    f.write('I am writing ..... All programs need to perform input and output. This chapter covers common idioms'
'for working with different kinds of files, including text and binary files, file encodings,'
'and other related matters. Techniques for manipulating filenames and directories are'
'also covered.')
    

f = open('test,txt' , 'rt') 
f.read()
