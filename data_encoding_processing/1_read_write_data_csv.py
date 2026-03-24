from collections import namedtuple
import csv

with open('stocks.csv') as f:
    f_read_csv = csv.reader(f)
    headers = next(f_read_csv)
    Row = namedtuple('Row' , headers) # dynamically creates a class Row and fiels come from the csv headers
    for r in f_read_csv:
        #  r   = ["AA",39.48,"6/11/2007","9:36am",-0.18,181800]
        # <--------------------------------------------------->
        #  row = Row("AA",39.48,"6/11/2007","9:36am",-0.18,181800)
        row = Row(*r)   # unpacks the list into arguments
        print(row)