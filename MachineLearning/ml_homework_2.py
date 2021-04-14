import pandas as pd

nyc = pd.read_csv("ave_yearly_temp_nyc_1895-2017.csv")
print(nyc.head(3))
print(nyc.Date.values)
print(nyc.Date.values.reshape(-1, 1))
print(nyc.Value.values)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1, 1), nyc.Value.values, random_state=11
)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
# The fit method expects the samples and the targets for training
linear_regression.fit(X=X_train, y=y_train)
print(linear_regression.coef_)
print(linear_regression.intercept_)
predicted = linear_regression.predict(X_test)
expected = y_test
for p, e in zip(predicted[::5], expected[::5]):
    print(f"predicted: {p:.2f}, expected: {e:.2f}")
predict = (
    lambda x: linear_regression.coef_ * x + linear_regression.intercept_
)  # y = mx + b


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

axes = sns.scatterplot(
    data=nyc,
    x="Date",
    y="Value",
    hue="Value",
    palette="winter",
    legend=False,
)
axes.set_ylim(10, 70)  # scale y-axis
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
print(x)
y = predict(x)
print(y)
line = plt.plot(x, y)
plt.show()