import csv
from datetime import datetime
#the date format used here is ISO 8601
dates = []
with open('src/filtered.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        value=" "
        start = 0
        x = 0
        for date in row[0]:
            # print(char+"\n"+ str(x))
            x+=1
            if date == ',':
                start += 1
            if start == 1 and date !=',':
                value += date
        print(value)
        dates.append(value)    
        # print(row)
dates.sort()
print("Below is first date")
#from this we can see CDC data tells us first case was 22nd Jan 2020
print(dates[0])