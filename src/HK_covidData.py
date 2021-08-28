import requests
import pandas as pd

# def get_data(url):
#     response = get(endpoint, timeout=10)
    
#     if response.status_code >= 400:
#         raise RuntimeError(f'Request failed: { response.text }')
        
#     return response.json()
    

# if __name__ == '__main__':
#     endpoint = ('https://api.data.gov.hk/v1/historical-archive/get-file?url=http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Flatest_situation_of_reported_cases_covid_19_eng.csv&time=20210827-0922'
#     )
    
#     data = get_data(endpoint)   
#     print(data)
url = 'https://api.data.gov.hk/v1/historical-archive/get-file?url=http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Flatest_situation_of_reported_cases_covid_19_eng.csv&time=20210827-0922'
response = requests.get(url)
response.raise_for_status()  # raises exception when not a 2xx response
if response.status_code != 204:
    print("Hello there")
    # print(response.csv())
data = response.content
print(data)
# data.to_csv()