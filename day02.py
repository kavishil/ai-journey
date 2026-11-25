import pandas as pd
import numpy as np 
df = pd.read_csv('C:\\Users\\Kavishil\\Downloads\\insurance.csv')
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.dtypes)
print(df.duplicated().sum())
print(df.describe())
df=df.drop_duplicates()
df.to_csv('insurance_cleaned.csv', index=False)

