#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
import numpy as np
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cdc.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("9mfq-cb36", limit=2000,state="NY")
# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df)
# when needed to generate an excel file
# results_df.to_excel('/home/siddarth/COMP4971C/src/filtered.xlsx')
results_df.to_csv('/home/siddarth/COMP4971C/src/filtered.csv')
# results_df