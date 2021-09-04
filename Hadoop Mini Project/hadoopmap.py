#!C:\Users\micha\anaconda3\python.exe

import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    
# [derive mapper output key values]
     line = line.strip()
     incident_id, incident_type, vin_number, make, model, year, Incident_year, description= line.split(",")

     results = [vin_number, incident_type, make, year]
     #print("\t".join(results))

     print('%s\t%s\t%s\t%s' %(vin_number,incident_type,make,year))