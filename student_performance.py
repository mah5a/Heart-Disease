from ucimlrepo import fetch_ucirepo
import pandas as pd

# # fetch dataset
# student_performance = fetch_ucirepo(id=320)
#
# # data (as pandas dataframes)
# X = student_performance.data.features
# y = student_performance.data.targets
#
# # metadata
# print(student_performance.metadata)
#
# # variable information
# print(student_performance.variables)
# print(X)


with open(r"D:\mahsa\LEARNING\PRACTICE\student-mat.csv", "r") as file:
    for _ in range(5):
        print(file.readline())

header = [ "school", "sex","age", "address","famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason",
           "guardian", "traveltime", "studytime", "failures", "schoolsup", "famsup", "paid", "activities", "nursery",
           "higher", "internet","romantic","famrel","freetime","goout", "Dalc","Walc","health""absences","G1", "G2","G3"]

# df = pd.read_csv(r"D:\mahsa\LEARNING\Data Analysis with Python\PRACTICE\heart+disease/new.data", header=None, names=columns)
df = pd.read_csv(r"D:\mahsa\LEARNING\PRACTICE\student-mat.csv",
                 delim_whitespace=True,  # استفاده از فاصله به عنوان جداکننده
                 header=None,
                 names=header)  # لیستی که قبلاً ساختیم
print(df.head())
print(df.shape)