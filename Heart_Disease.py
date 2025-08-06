import pandas as pd
import numpy as np

# from ucimlrepo import fetch_ucirepo
#
# # fetch dataset
# heart_disease = fetch_ucirepo(id=45)
#
# # data (as pandas dataframes)
# X = heart_disease.data.features
# y = heart_disease.data.targets
#
# # metadata
# print(heart_disease.metadata)
#
# # variable information
# print(heart_disease.variables)

with open(r"D:\mahsa\LEARNING\PRACTICE\new.data", "r") as file:
    for _ in range(5):
        print(file.readline())

columns = [
    'id', 'ccf', 'age', 'sex', 'painloc', 'painexer', 'relrest', 'pncaden', 'cp',
    'trestbps', 'htn', 'chol', 'smoke', 'cigs', 'years', 'fbs', 'dm', 'famhist',
    'restecg', 'ekgmo', 'ekgday', 'ekgyr', 'dig', 'prop', 'nitr', 'pro', 'diuretic',
    'proto', 'thaldur', 'thaltime', 'met', 'thalach', 'thalrest', 'tpeakbps',
    'tpeakbpd', 'dummy', 'trestbpd', 'exang', 'xhypo', 'oldpeak', 'slope',
    'rldv5', 'rldv5e', 'ca', 'restckm', 'exerckm', 'restef', 'restwm', 'exeref',
    'exerwm', 'thal', 'thalsev', 'thalpul', 'earlobe', 'cmo', 'cday', 'cyr',
    'num', 'lmt', 'ladprox', 'laddist', 'diag', 'cxmain', 'ramus', 'om1', 'om2',
    'rcaprox', 'rcadist', 'lvx1', 'lvx2', 'lvx3', 'lvx4', 'lvf', 'cathef', 'junk', 'name'
]
# df = pd.read_csv(r"D:\mahsa\LEARNING\Data Analysis with Python\PRACTICE\heart+disease/new.data", header=None, names=columns)
df = pd.read_csv(r"D:\mahsa\LEARNING\PRACTICE\new.data",
                 delim_whitespace=True,  # use space as seperator
                 header=None,
                 names=columns)
# df.to_csv("D:\mahsa\LEARNING\PRACTICE\heart_disease.csv")

# Inspect the Data
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None)
print("\n-----------------------------\n Verify successful load with some randomly selected "
      "records\n -----------------------------\n", df.sample(5))
print("\n-----------------------------\n SHOW TOP 5 ROW OF DATA RECORDS: \n-----------------------------\n", df.head())

print("\n ---------------------------\n STATISTICAL SUMMARY OF THE DATA\n------------------------------\n ",
      df.describe())
print("\n ---------------------------\n Dimensions of the data:\n------------------------------------\n", df.shape)
print("\n ---------------------------\n Information about data\n ---------------------------\n", df.info)

df1 = df.replace('?', np.NaN)
df_empty_columns = df.dropna(axis=1, how='all')

df_empty_rows = df_empty_columns.dropna(axis=0)
print(df_empty_rows.isna().sum())
print("\n ---------------------------\n Dimensions of the data:\n------------------------------------\n",
      df_empty_rows.shape)
df_invalid = df_empty_rows.replace('-9', np.NaN)
df_clean = df_invalid.dropna(axis=0)
print("\n ---------------------------\n Dimensions of the data:\n------------------------------------\n",
      df_clean.shape)
