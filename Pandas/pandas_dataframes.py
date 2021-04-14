import pandas as pd


grades_dict = {'Wally': [87,96,70],
               'Eva': [100,87,90],
               'Sam': [94,77,90],
               'Katie': [100,81,82],
               'Bob': [83,65,85]}


#print(grades_dict)
#output:
#{'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}


grades = pd.DataFrame(grades_dict)
#print(grades)
#output:
#   Wally  Eva  Sam  Katie  Bob
#0     87  100   94    100   83
#1     96   87   77     81   65
#2     70   90   90     82   85


#To change the indices and customize them:
grades.index = ['Test1','Test2','Test3']
#print(grades)
#output:
#       Wally  Eva  Sam  Katie  Bob
#Test1     87  100   94    100   83
#Test2     96   87   77     81   65
#Test3     70   90   90     82   85
#print(grades['Eva'])
#output:
#Test1    100
#Test2     87
#Test3     90
#Name: Eva, dtype: int64
#print(grades.Sam)
#output:
#Test1    94
#Test2    77
#Test3    90
#Name: Sam, dtype: int64



####################################
#          loc and iloc            #
####################################
#loc        #Location method
#print(grades.loc['Test1'])
#output:
#Wally     87
#Eva      100
#Sam       94
#Katie    100
#Bob       83
#Name: Test1, dtype: int64

#iloc       #item/index Location method 
#ZERO BASED - just like indices, starts at 0
#print(grades.iloc[1])
#output:
#Wally    96
#Eva      87
#Sam      77
#Katie    81
#Bob      65
#Name: Test2, dtype: int64


#Slicing with loc INCLUDES the upper limit since its not dealing with indexes but rather with values
#print(grades.loc['Test1':'Test3'])
#output:
#       Wally  Eva  Sam  Katie  Bob
#Test1     87  100   94    100   83
#Test2     96   87   77     81   65
#Test3     70   90   90     82   85


#Slicing with iloc DOES NOT INCLUDE the upper limit since its index based
#print(grades.iloc[0:2])
#output:
#       Wally  Eva  Sam  Katie  Bob
#Test1     87  100   94    100   83
#Test2     96   87   77     81   65



#Non-sequential JUST Test1 and Test3
#print(grades.loc[['Test1','Test3']])
#output:
#       Wally  Eva  Sam  Katie  Bob
#Test1     87  100   94    100   83
#Test3     70   90   90     82   85
#print(grades.iloc[[0,2]])
#output:
#       Wally  Eva  Sam  Katie  Bob
#Test1     87  100   94    100   83
#Test3     70   90   90     82   85


# View only Eva and Katie's grades for Test1 and Test2

#print(grades.loc['Test1':'Test2', ['Eva','Katie']])
#output:
#       Eva  Katie
#Test1  100    100
#Test2   87     81

#print(grades.iloc[0:2,[1,3]])
#output:
#       Eva  Katie
#Test1  100    100
#Test2   87     81


above_90 = grades[grades>90]
#print(above_90)
#output:
#       Wally    Eva   Sam  Katie  Bob
#Test1    NaN  100.0  94.0  100.0  NaN
#Test2   96.0    NaN   NaN    NaN  NaN
#Test3    NaN    NaN   NaN    NaN  NaN


b_grades = grades[(grades>=80)&(grades<90)]
#print(b_grades)
#output:
#       Wally   Eva  Sam  Katie   Bob
#Test1   87.0   NaN  NaN    NaN  83.0
#Test2    NaN  87.0  NaN   81.0   NaN
#Test3    NaN   NaN  NaN   82.0  85.0


#print(grades.at['Test2','Eva'])
#output: 87
#print(grades.iat[1,2])
#output: 77

grades.at['Test2','Eva'] = 100
#print(grades)
#output:
#       Wally  Eva  Sam  Katie  Bob
#Test1     87  100   94    100   83
#Test2     96  100   77     81   65
#Test3     70   90   90     82   85


#print(grades.describe())
#output:          
#           Wally         Eva        Sam       Katie        Bob
#count   3.000000    3.000000   3.000000    3.000000   3.000000
#mean   84.333333   96.666667  87.000000   87.666667  77.666667
#std    13.203535    5.773503   8.888194   10.692677  11.015141
#min    70.000000   90.000000  77.000000   81.000000  65.000000
#25%    78.500000   95.000000  83.500000   81.500000  74.000000
#50%    87.000000  100.000000  90.000000   82.000000  83.000000
#75%    91.500000  100.000000  92.000000   91.000000  84.000000
#max    96.000000  100.000000  94.000000  100.000000  85.000000


pd.set_option('precision', 2)
#print(grades.describe())
#output:
#       Wally     Eva    Sam   Katie    Bob
#count   3.00    3.00   3.00    3.00   3.00
#mean   84.33   96.67  87.00   87.67  77.67
#std    13.20    5.77   8.89   10.69  11.02
#min    70.00   90.00  77.00   81.00  65.00
#25%    78.50   95.00  83.50   81.50  74.00
#50%    87.00  100.00  90.00   82.00  83.00
#75%    91.50  100.00  92.00   91.00  84.00
#max    96.00  100.00  94.00  100.00  85.00



################
#   Transpose  #
################


#print(grades.T.describe())
#output:
#        Test1   Test2  Test3
#count    5.00    5.00   5.00
#mean    92.80   83.80  83.40
#std      7.66   14.31   8.23
#min     83.00   65.00  70.00
#25%     87.00   77.00  82.00
#50%     94.00   81.00  85.00
#75%    100.00   96.00  90.00
#max    100.00  100.00  90.00

#print(grades.T.mean())
#output:
#Test1    92.8
#Test2    83.8
#Test3    83.4
#dtype: float64



#############################################
#                   SORTING                 #
#############################################



grades.sort_index(ascending=False) #descending order
print(grades)


grades.sort_index(axis=1)
print(grades)


grades.sort_values(by='Test1', axis=1, ascending=False)
print(grades)