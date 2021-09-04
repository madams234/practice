#!C:\Users\micha\anaconda3\python.exe

import sys
 
# Create a dictionary to map words to counts
accidentrecord = {}
 
# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip()
 
    # parse the input from mapper.py
    line= line.split('\t')
    make=line[0]
    year=line[1]
    count=line[2]

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        accidentrecord[(make,year)] = accidentrecord[(make,year)]+count
    except:
        accidentrecord[(make,year)] = count
 
# Write the tuples to stdout
# Currently tuples are unsorted
for make,year in accidentrecord.keys():
    print('%s\t%s\t%s' %(make,year, accidentrecord[(make,year)]))