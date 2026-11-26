import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(url)

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.dtypes)
print(df.columns)
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols]= df[cols].replace(0,np.nan)
print(df.isna().sum())
df[cols]=df[cols].fillna(df[cols].median())
print(df.isna().sum())
print(df.shape)
df.to_csv('day03_cleaned.csv', index=False)
print("saved")



