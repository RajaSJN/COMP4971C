from datetime import date
from re import sub
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.arrays.integer import Int16Dtype
from sodapy import Socrata
# in place of application token, and no username or password:
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
new_cases = results_df['new_case'][::20]
dates = results_df['submission_date'][::20]
# print(new_cases.cat)
print(type(new_cases))
# new_cases= new_cases.values
# dates = dates.values
print(new_cases)
print(dates)
# results_df.reindex(new_cases)
results_df.to_csv('/home/siddarth/COMP4971C/src/filtered.csv')
# results_df
link = 'https://data.cdc.gov/resource/gxj9-t96f.json'
vaccine_result = client.get("gxj9-t96f",limit=2000)
vaccine_df = pd.DataFrame.from_records(vaccine_result)
# new_covid = vaccine_df[]
print(vaccine_df)
x=dates.values.tolist()
print("this is x ")
print(len(x))