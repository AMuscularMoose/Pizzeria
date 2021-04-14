import pandas as pd
from sklearn.datasets import fetch_california_housing


california = fetch_california_housing()  # Bunch object

# print(california.DESCR)
# print(california.data.shape)
# print(california.target.shape)
# print(california.feature_names)

pd.set_option("precision", 4)  # 4 digit precision for floats
pd.set_option("max_columns", 9)  # display up to 9 columns in DataFrame outputs
pd.set_option("display.width", None)  # auto-detect the display width for wrapping

# creates the initial DataFrame using the data in california.data and with the
# column names specified based on the features of the sample
california_df = pd.DataFrame(california.data, columns=california.feature_names)
# add a column to the DataFrame for the median house values stored in california.target
california_df["MedHouseValue"] = pd.Series(california.target)
# print(california_df.head())  # peek at the first 5 rows
# using the describe method of datafreames we can get some statistical info
# print(california_df.describe())

# The keyword argument frac specifies the fraction of the data to select (0.1 for 10%),
# and the keyword argument random_state enables you to seed the random number generator
# this allows you to reproduce the same 'randomly' selected rows
sample_df = california_df.sample(frac=0.1, random_state=17)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=2)
sns.set_style("whitegrid")
"""
for feature in california.feature_names:
    plt.figure(figsize=(8, 4.5))  # 8" - by - 4.5" Figure
    sns.scatterplot(
        data=sample_df,
        x=feature,
        y="MedHouseValue",
        hue="MedHouseValue",
        palette="cool",
        legend=False,
    )

plt.show()
"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    california.data, california.target, random_state=11
)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)

for i, name in enumerate(california.feature_names):
    print(f"{name}: {linear_regression.coef_[i]}")

predicted = linear_regression.predict(X_test)
expected = y_test
print(predicted[:5])
print(expected[:5])

# create a DataFrame containing columns for the expected and predicted values:
df = pd.DataFrame()
df["Expected"] = pd.Series(expected)
df["Predicted"] = pd.Series(predicted)
print(df[:10])

# plot the data as a scatterplot with the expected (target) prices along the x-axis and the predicted prices along the y-axis:
import matplotlib.pyplot as plt2

figure = plt2.figure(figsize=(9, 9))

axes = sns.scatterplot(
    data=df, x="Expected", y="Predicted", hue="Predicted", palette="cool", legend=False
)

# set the x- and y-axes' limits to use the same scale along both axes:
start = min(expected.min(), predicted.min())
print(start)
end = max(expected.max(), predicted.max())
print(end)

axes.set_xlim(start, end)
axes.set_ylim(start, end)

# the following snippet displays a line between the points representing the lower-left corner of the graph (start, start)
# and the upper-right corner of the graph (end, end). The third argument ('k--') indicates the line's style. the letter k
# represents the color black, and the -- indicates that plot should draw a dashed line:

line = plt2.plot([start, end], [start, end], "k--")

plt2.show()