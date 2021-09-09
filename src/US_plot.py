from datetime import date
from re import sub
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.arrays.integer import Int16Dtype
from sodapy import Socrata
import yfinance as yf 
# The following library is needed for calculating the pearson correlation 
from scipy.stats import pearsonr
# The following library is needed for calculating the Spearman's correlation 
from scipy.stats import spearmanr
client = Socrata("data.cdc.gov", None)
# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("9mfq-cb36", limit=2000,state="NY")
# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df = results_df.sort_values(by='submission_date')
# when needed to generate an excel file
# results_df.to_excel('/home/siddarth/COMP4971C/src/filtered.xlsx')
#to filter based on column
# print(results_df)
#[::20] will be used as a basic smoothening factor for the curve    
new_cases = results_df['new_case'][::20]
dates = results_df['submission_date'][::20]
print(new_cases.values)
print(dates)
results_df.to_csv('/home/siddarth/COMP4971C/src/filtered.csv')
x=dates.values.tolist()
print("this is x ")
print(len(x))
temp = []
for i in new_cases.values:
    temp.append(float(i))
new = pd.Series(temp, index=dates)
plot1=plt.figure(1)
plot1.suptitle('Covid cases', fontsize=10)
#This is how you name axis
plt.xlabel('Date', fontsize=10)
new.plot()
link = 'https://data.cdc.gov/resource/8xkx-amqh.json'
vaccine_result = client.get("8xkx-amqh",limit=2000,recip_state="NY",recip_county="Dutchess County")
vaccine_df = pd.DataFrame.from_records(vaccine_result)
vaccine_df = vaccine_df.sort_values(by='date')
vaccine_df.to_csv('/home/siddarth/COMP4971C/src/us_vaccine.csv')
plot2 = plt.figure(2)
#the following code is for how to set the figure label and other characteristics
plot2.suptitle('Vaccination', fontsize=10)
plt.xlabel('Date', fontsize=10)
vaccine_temp =[]
for i in vaccine_df["series_complete_yes"][::20]:
    vaccine_temp.append(float(i))
plt.plot(vaccine_df["date"][::20],vaccine_temp)
plot3 = plt.figure(3)
Nvidia = yf.download(tickers='NVDA', start="2020-01-22", interval='1d')
Amd = yf.download(tickers='AMD', start="2020-01-22", interval='1d')
Ubisoft = yf.download(tickers='UBI', start="2020-01-22", interval='1d')
Activision = yf.download(tickers='ATVI', start="2020-01-22", interval='1d')
Tesla = yf.download(tickers='TSLA',start="2020-01-22", interval='1d')
plot3.suptitle('NYSE Data', fontsize=10)
plt.xlabel('Date', fontsize=10)
print(Nvidia)
plt.plot(Nvidia['Adj Close'])
plt.plot(Amd['Adj Close'])
plt.plot(Ubisoft['Adj Close'])
plt.plot(Activision['Adj Close'])
plt.plot(Tesla['Adj Close'])
print(len(Nvidia['Adj Close'].values))
print(len(results_df['new_case'].values))
#since not all days in the year are trading days, we have to filter out non trading days data for analysis, no data on weekends
filteredNewCases= []
print(type(Nvidia))
print(type(Nvidia.index[0]))
print(results_df['submission_date'][0][0:10:1])
print(str(Nvidia.index[0])[0:10:1])
print(str(Nvidia.index[0])[0:10:1]==results_df['submission_date'][0][0:10:1])
print(type(results_df['submission_date']))
temp = results_df['submission_date'].to_list()
casesList = results_df['new_case'].to_list()
print(casesList)
counter =-1
filteredDates = []
for i in temp:
    counter +=1
    for j in Nvidia.index:
        value = str(j)[0:10:1]
        if (value == i[0:10:1]):
            filteredNewCases.append(float(casesList[counter]))
            filteredDates.append(i)
            break
print(len(filteredNewCases))
print(len(Nvidia['Adj Close'].values))
print(filteredDates)
NvidiaStockValues = Nvidia['Adj Close'].values
pearsCor, _ = pearsonr(NvidiaStockValues[0:len(filteredNewCases)], filteredNewCases)
spearCor, _ = spearmanr(NvidiaStockValues[0:len(filteredNewCases)], filteredNewCases)
print("The pearson is " +str(pearsCor) + "The spearmen is "+ str(spearCor))
#The following line is required to actually display the graphs
plt.show()