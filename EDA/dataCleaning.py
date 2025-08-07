import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
pd.set_option('display.max_columns',200)

df = pd.read_csv('C:\\Users\\Priya\\OneDrive\\Desktop\\vsCode\\ML\\EDA\\expected_ctc.csv')
#print(df.head)
print(df.columns)
DropColumns=['IDX',
    'Applicant_ID',
    'Expected_CTC',
    'Current_CTC',
    'Inhand_Offer',
    'Curent_Location',
    'Preferred_location',
    'University_Grad',
    'University_PG',
    'University_PHD',
    'Passing_Year_Of_Graduation',
    'Passing_Year_Of_PG',
    'Passing_Year_Of_PHD',
    'Organization',
    'Designation']

print(df.drop(DropColumns, axis=1,inplace =True))
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
print(df.isna().sum())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
