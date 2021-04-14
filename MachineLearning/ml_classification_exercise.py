# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features.
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris
# virginica. Each sample’s features are the sepal length, sepal width, petal
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower
# that protect the smaller inside petals before the flower buds bloom.

# EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

iris = load_iris()
print(iris.DESCR)
# print(iris.target_names)

names = ["Setosa", "Versicolor", "Virginica"]
data_train, data_test, target_train, target_test = train_test_split(
    iris.data, iris.target, random_state=11
)
knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train)
predicted = knn.predict(data_test)
expected = target_test

# display the shape of the data, target and target_names

print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)

predicted = [iris.target_names[i] for i in predicted]
expected = [iris.target_names[i] for i in expected]
print(predicted[:10])
print(expected[:10])

# display the values that the model got wrong

wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print(wrong)
print(format(knn.score(data_test, target_test), ".2%"))
confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)

# visualize the data using the confusion matrix

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

confusion_df = pd.DataFrame(confusion, index=range(3), columns=range(3))
figure = plt.figure()
axes = sns.heatmap(confusion_df, annot=True, cmap=plt.cm.nipy_spectral_r)
plt.show()
