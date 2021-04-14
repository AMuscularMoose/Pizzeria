import pandas as pd


#A Series is a 1-dimensional array
grades = pd.Series([87,100,94])
#print(grades)
#output:
#0     87    
#1    100    
#2     94    
#dtype: int64


same_grade = pd.Series(98.6, range(3))
#print(same_grade)
#output:
#0      98.6
#1      98.6
#2      98.6
#dtype: float64


#Using NumPy methods:
a = grades[0]
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()


# Calling Series method describe produces all these stats and more:
grades.describe()


grades = pd.Series([87,100,94], index=['Wally','Eva','Sam'])
#print(grades)
#output:
#Wally     87
#Eva      100
#Sam       94
#dtype: int64


# If you initialize a Series with a dictionary, its keys become the 
# Series' indices, and its values become the Series' element values:

grades = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})
#this and the series above are THE SAME


# you can access individual elements via square brackets
# containing a custom index value:
#print(grades['Eva'])
#output: 100


# If the custom indices are strings that could represent valid Python indentifiers,
# pandas automatically adds them to the Series as attributes that you can access
# via a dot (.), as in:

#grades.Wally
#output: 87


#Series also has built-in attributed. For example, the dtype attribute returns
# the underlying array's element type:
#grades.dtype()
#dtype('int64')


#grades.values
#array([ 87, 100, 94])


#Series of Strings:
hardware = pd.Series(['Hammer','Saw','Wrench'])
#print(hardware)
#output:
#0    Hammer  
#1       Saw  
#2    Wrench  
#dtype: object


answer = hardware.str.contains('a')
#print(answer)
#output:
#0     True
#1     True
#2    False
#dtype: bool


hardware_upper = hardware.str.upper()
#print(hardware_upper)
#output:
#0    HAMMER
#1       SAW
#2    WRENCH
#dtype: object


