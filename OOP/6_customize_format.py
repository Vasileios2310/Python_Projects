_formats = {
'ymd' : '{d.year}-{d.month}-{d.day}',
'mdy' : '{d.month}/{d.day}/{d.year}',
'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self , year , month , day):
        self.year = year
        self.month = month
        self.day = day
        
    def __format__(self, code):
        if code == '':
            code= 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
    
d = Date(2026 , 3 , 28)
d1 = format(d)
print(d1)

d2 = format(d , 'mdy')
print(d2)

print('The date is {:dmy}'.format(d))