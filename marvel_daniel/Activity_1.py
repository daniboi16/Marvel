'''
    @File:  Activity_1.py
    @Author:    Daniel Joseph ALapat on VS code VM
    @Descrition:    Python code for activity 1
'''
## Importing Required liabraries
import requests
import hashlib
import json
import pandas as pd
from string import ascii_lowercase

## Saving API data into variables
#TODO make keys more secure by saving in gitignore file
daniel_public_key = "85f0825685496e19d6d3e0afa53be741"
daniel_private_key = "9f9a00cac4693f94986777058375e98a6a1ac3fb"
charecters_address = "https://gateway.marvel.com:443/v1/public/characters"
charecters_ts = 1

## Hasing the key
charecters_hash = hashlib.md5((str(charecters_ts)+daniel_private_key+daniel_public_key).encode()).hexdigest()

'''
## Setting the parameters
charecters_parameters = {
    "apikey" : daniel_public_key,
    "ts" : charecters_ts,
    "hash" : charecters_hash
}
## Calling Api
charecters_response = requests.get(charecters_address, params= charecters_parameters)
charecters_results = charecters_response.json()
'''

## Converting to pandas df
charecters_df = pd.DataFrame()
## Calling with dynamic parameters
for i in ascii_lowercase:
    charecters_parameters = {
    "apikey" : daniel_public_key,
    "ts" : charecters_ts,
    "hash" : charecters_hash,
    "limit" : 100,
    "nameStartsWith" : i }
    charecters_response = requests.get(charecters_address, params=charecters_parameters)
    charecters_results = charecters_response.json()
    df = pd.json_normalize(charecters_results['data'],['results'])
    df = df[['id','name','comics.available','events.available','stories.available','series.available']]
    charecters_df = charecters_df.append(df)
