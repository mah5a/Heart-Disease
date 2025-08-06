import pandas as pd
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

with open(r"D:\mahsa\LEARNING\Data Analysis with Python\PRACTICE\heart+disease\new.data", "r") as file:
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
df = pd.read_csv(r"D:\mahsa\LEARNING\Data Analysis with Python\PRACTICE\heart+disease/new.data",
                 delim_whitespace=True,  # استفاده از فاصله به عنوان جداکننده
                 header=None,
                 names=columns)  # لیستی که قبلاً ساختیم
print(df.head())
print(df.shape)
