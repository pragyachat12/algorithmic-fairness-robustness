#to get accustomed to the data and do some basic EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns      


# Load the dataset
df = pd.read_csv('data/data.csv')

FEATURE_COLS = [
    'age',
    'juv_fel_count',
    'juv_misd_count', 
    'juv_other_count',
    'priors_count',
    'days_b_screening_arrest',
    'c_charge_degree'
]

LABEL_COL = 'two_year_recid'
# Display the first few rows of the dataset
print(df.head())
# Get summary statistics of the dataset
print(df.describe())
# Check for missing values
print(df.isnull().sum())


# basic info
print(df.shape)
print(df[['race', 'sex', 'two_year_recid']].value_counts())

# recidivism rate by race
print(df.groupby('race')['two_year_recid'].mean())

# check for nulls in your feature cols
print(df[FEATURE_COLS + ['two_year_recid', 'race']].isnull().sum())

