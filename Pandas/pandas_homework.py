import pandas as pd
import numpy as np

#1. Create a Series from the list [7, 11, 13, 17].
series1 = pd.Series([7,11,13,17])
print(series1)


#2. Create a Series with five elements that are all 100.0.
same_series = pd.Series(100, range(5))
print(same_series)


#3. Create a Series with 20 elements that are all random numbers in the range 0 to 100.
#    Use method describe to produce the Series’ basic descriptive statistics.
rand_series = pd.Series(np.random.randint(0,101,20))
print(rand_series.describe())


#4. Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. 
#    Using the index keyword argument, specify the custom indices:
#    'Julie', 'Charlie', 'Sam' and 'Andrea'.
temperatures = pd.Series([98.6,98.9,100.2,97.9], index=['Julie','Charlie','Sam','Andrea'])
print(temperatures)


#5. Form a dictionary from the names and values in Part (4), 
#    then use it to initialize a Series.
tempDict = pd.Series({'Julie':98.6, 'Charlie':98.9, 'Sam':100.2, 'Andrea':97.9})
print(tempDict)

