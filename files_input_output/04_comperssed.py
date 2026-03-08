import gzip

text = ''

with gzip.open('somefile.gz' , 'wt') as f:
    f.write(text)