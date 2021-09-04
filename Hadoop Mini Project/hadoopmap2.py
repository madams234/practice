#!C:\Users\micha\anaconda3\python.exe

import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
# [derive mapper output key values]
    line = line.strip()

    # parse the input we got from mapper.py
    line = line.split('\t')
    make=line[1]
    year=line[2]

    print('%s\t%s\t%d' %(make,year,1))