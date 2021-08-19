import requests
import json
import csv

url = 'https://metals-api.com/api/timeseries?access_key=*******************&start_date=2019-08-05&end_date=2020-08-01&base=USD&symbols=XAU'

r = requests.get(url).json()

#x = json.load()
file = open('XAUInfo.txt', 'a')
for date in r['rates']:
    file.write(date)
    file.write(' ')
    file.write(str(r['rates'][date]['XAU']))
    file.write('\n')
file.close()