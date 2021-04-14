from sklearn.datasets import load_digits


digits = load_digits()
"""
# print(digits.DESCR)
print(digits.data[13])
# output is a 1-dimentional array
print(digits.data.shape)
# output = (1797, 64)
# 1797 samples (rows)
# 64 features (columns)
print(digits.target[13])
# output = 3
# means the target is just the number 3
print(digits.target.shape)
# output = (1797,)
# same amount of rows but just 1 column or feature(target)
print(digits.images[13])
# data is a multi-dimentional array


import matplotlib.pyplot as plt

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
# python zip function bundles the 3 iterables and produces one iterable
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item  # produces one iterable
    axes.imshow(
        image, cmap=plt.cm.gray_r
    )  # displays multichannel (RGB) or single-channel ("grayscale") image data
    axes.set_xticks([])  # remove x-axis tick marks
    axes.set_yticks([])  # remove y-axis tick marks
    axes.set_title(target)  # the target value of the image
plt.tight_layout()
plt.show()
"""


from sklearn.model_selection import train_test_split


data_train, data_test, target_train, target_test = train_test_split(
    digits.data, digits.target, random_state=11
)
# random_state for reproducibility.
print(data_train.shape)
# (1347, 64)
print(target_train.shape)
# (1347,)
print(data_test.shape)
# (450, 64)


from sklearn.neighbors import KNeighborsClassifier


knn = KNeighborsClassifier()
# Load the training data into the model using the fit method
# Note: the KNeighborsClassifier fit method does not do calculations,
# it just loads the model
knn.fit(X=data_train, y=target_train)
# Returns an array containing the predicted class of each test image:
# creates an array of digits
predicted = knn.predict(X=data_test)
expected = target_test
print(predicted[:20])
print(expected[:20])
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print(wrong)
# output is a list of tuples:
# [(5, 3), (8, 9), (4, 9), (7, 3), (7, 4), (2, 8), (9, 8), (3, 8), (3, 8), (1, 8)]
print(format(knn.score(data_test, target_test), ".2%"))
# 97.78%


from sklearn.metrics import confusion_matrix


confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2


confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
figure = plt2.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.show()
