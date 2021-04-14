import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

cal_housing = fetch_california_housing()
# print(cal_housing.DESCR)
print(cal_housing.data.shape)
print(cal_housing.target.shape)
print(cal_housing.target_names)
print(cal_housing.feature_names)

pd.set_option("precision", 4)
pd.set_option("max_columns", 9)
pd.set_option("display.width", None)

cal_housing_df = pd.DataFrame(cal_housing.data, columns=cal_housing.feature_names)
cal_housing_df["MedHouseValue"] = pd.Series(cal_housing.target)

print(cal_housing_df.head())
print(cal_housing_df.describe())
print(cal_housing_df["MedHouseValue"].describe())

sns.set(font_scale=1.1)
sns.set_style("whitegrid")

figure = plt.figure()
grid = sns.pairplot(data=cal_housing_df, vars=cal_housing_df.columns[0:8])
plt.show()