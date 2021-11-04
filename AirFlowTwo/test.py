from pathlib import Path

log_dir="C:\\airflowlogs\\marketvol\\"

file_list = Path(log_dir).rglob('*.log')

for file in file_list:
    print(file)

#with open(log_dir) as f:
 #   dict1=parse_logs(f)
  #  print("The total number of errors :" +str(len(dict1)))
   # print("Here are all the errors: ")
    #if len(dict1) > 0:    
     #   for i in range(len(dict1)):
      #      print(dict1[i])