import pandas as pd
import numpy as np
import openpyxl

def preprocess(voters):
    # load dataset
    voters = pd.read_excel('votersconstituency-2.xlsx')
    
    # Let's replace the empty strings with NaN values
    voters = voters.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    voters = voters.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    voters = voters.replace('.', np.nan)
    
    # drop null columns
    voters.dropna(inplace=True)
    
    # rename columns
    voters.rename(columns={'REGISTERED VOTERS PER CONSTITUENCY FOR 2017 GENERAL ELECTIONS':'COUNTY_CODE', 'Unnamed: 1':'COUNTY_NAME', 
                    'Unnamed: 2':'CONST_CODE', 'Unnamed: 3':'CONSTITUENCY_NAME', 'Unnamed: 4':'VOTERS', 'Unnamed: 5':'NO. OF POLLING STATIONS'}, inplace=True)
    
    # drop the column
    voters.drop(axis=0, index=0)
    
    # convert to numerical columns, ---- VOTERS,	NO. OF POLLING STATIONS
    voters['VOTERS'] = pd.to_numeric(voters['VOTERS'], errors='coerce')
    voters['NO. OF POLLING STATIONS'] = pd.to_numeric(voters['NO. OF POLLING STATIONS'], errors='coerce')
    voters['CONST_CODE'] = pd.to_numeric(voters['CONST_CODE'], errors='coerce')
    voters['COUNTY_CODE'] = pd.to_numeric(voters['COUNTY_CODE'], errors='coerce')
    
    # check for duplicate rows in the dataset -> 
    voters.duplicated().sum()
    
    # check missing values -> 
    voters.isnull().sum()
    
    # drop missing rows ->
    voters.dropna(inplace=True)
    
    # convert to integer.
    voters['VOTERS'] = voters['VOTERS'].astype(int)
    voters['NO. OF POLLING STATIONS'] = voters['NO. OF POLLING STATIONS'].astype(int)
    voters['COUNTY_CODE'] = voters['COUNTY_CODE'].astype(int)
    voters['CONST_CODE'] = voters['CONST_CODE'].astype(int)
    
    return voters