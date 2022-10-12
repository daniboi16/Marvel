'''
    @File:  Activity_4.py
    @Author:    Daniel Joseph ALapat on VS code VM
    @Descrition:    Python code for activity 4
'''
## Importing Required liabraries
import requests
import hashlib
import json
import pandas as pd

## Saving API data into variables
daniel_public_key = "85f0825685496e19d6d3e0afa53be741"
daniel_private_key = "9f9a00cac4693f94986777058375e98a6a1ac3fb"
charecters_address = "https://gateway.marvel.com:443/v1/public/characters"
charecters_ts = 1
charecters_hash = hashlib.md5((str(charecters_ts)+daniel_private_key+daniel_public_key).encode()).hexdigest()
results_df = pd.DataFrame()

'''
    @Description:   Fucntion creats a dataframe by calling API
    @Param: API Key
    @Param: Hash
    @Param: Name starts with
'''
def create_dataframe(API_key = daniel_public_key, Hash =charecters_hash, name_starts_with = "a"):
    parameters = {
    "apikey" : API_key,
    "ts" : charecters_ts,
    "hash" : Hash,
    "limit" : 100,
    "nameStartsWith" : name_starts_with }
    charecters_response = requests.get(charecters_address, params=parameters)
    charecters_results = charecters_response.json()
    df = pd.json_normalize(charecters_results['data'],['results'])
    df = df[['id','name','comics.available','events.available','stories.available','series.available']]
    charecters_df = pd.DataFrame()
    charecters_df = charecters_df.append(df)
    return charecters_df


'''
    @Description:   Fucntion that filters df based on column provided
    @Param: data frame
    @Param: Column name
    @Param: Filter condition
    @Param: Filter Value
'''
def filter_df(data_frame,column_name,filter_condition,filter_value):
    if column_name == "name":
        return(data_frame[data_frame.name.str[:len(filter_value)] == filter_value])
    if filter_condition == 'equal_to':
        return(data_frame[data_frame[column_name] == filter_value])
    if filter_condition == 'less_than':
        return(data_frame[data_frame[column_name] < filter_value])
    if filter_condition == 'greater_than':
        return(data_frame[data_frame[column_name] > filter_value])
    return("ERROR")

results_df = create_dataframe(daniel_public_key,charecters_hash,"b")
print(filter_df(results_df,"name","equal_to","Balder"))