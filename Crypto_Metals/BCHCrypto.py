import csv
import requests

API_KEY = '*************'
API_Function = 'function=TIME_SERIES_INTRADAY_EXTENDED'
url = 'https://www.alphavantage.co/query?'
API_symbol = '&symbol'

# https://www.alphavantage.co/support/#api-key (8/18/21)
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=BCH&interval=15min&slice=year1month1&apikey=***************'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    my_list.pop(0)
    BCH = open('BCHInfo.txt', 'a')
    for row in my_list:
        list_to_string = ' '.join([str(elem) for elem in row])
        BCH.write(list_to_string + '\n')
    BCH.close()

