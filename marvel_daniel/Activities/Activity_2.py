'''
    @File:  Activity_2.py
    @Author:    Daniel Joseph ALapat on VS code VM
    @Descrition:    Python code for activity 2
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
## Hasing the key
charecters_hash = hashlib.md5((str(charecters_ts)+daniel_private_key+daniel_public_key).encode()).hexdigest()
## Converting to pandas df
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

results_df = create_dataframe(daniel_public_key,charecters_hash,"b")
print(results_df)