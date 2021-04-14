import numpy as np


'''
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

#ROWS - grades for each student
#COLS - grades for each test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
print("Avg of each test: \n",g)

h = grades.mean(axis=1)
print("Avg of each student: \n",h)



numbers = np.array([1,4,9,16,25,36])

sqrt = np.sqrt(numbers)
#print(sqrt)
#output = [1. 2. 3. 4. 5. 6.]

numbers2 = np.arange(1,7) * 10      #Broadcasting
#print(numbers2)
#output = [10 20 30 40 50 60]

add = np.add(numbers,numbers2)      #adding the two arrays
#print(add)
#output = [11 24 39 56 75 96]

multiply = np.multiply(numbers2,5)  #multiplying values of numbers2 array by 5
#print(multiply)
#output = [ 50 100 150 200 250 300]

numbers3 = numbers2.reshape(2,3)
numbers4 = np.array([2,4,6])
multiply2 = np.multiply(numbers3,numbers4)
print(multiply2)
'''
'''
This works because numbers4 has the same length as each row of numbers3, so NumPy can apply the multiply operation
by treating numbers4 as if it were the following array:

array([[2, 4, 6],[2, 4, 6]])
'''


#############################################
#           INDEXING AND SLICING            #
#############################################

grades = np.array([[87,96,70],[100,87,90],
                   [94,77,90],[100,81,82]])

a = grades[0,1]
#print(a)
#output = 96

b = grades[1]
#print(b)
#output = [100  87  90]

# To select multiple sequential rows use slice notation (remember upper limit is not included)
first_two = grades[0:2]     #since upper limit is not included, row 2 isnt there
#print(first_two)
#output = [[ 87  96  70]
#          [100  87  90]]

# To select multiple NON-sequential rows use a list of row indicies:
nonSeq = grades[[1,3]]
#print(nonSeq)
#output = [[100  87  90]
#          [100  81  82]]

# All rows and only first column
c = grades[:,0]
#print(c)
#output = [ 87 100  94 100]

# You can select consecutive columns using a slice:
d = grades[:,1:3]
#print(d)
#output = [[96 70] 
#          [87 90] 
#          [77 90] 
#          [81 82]]

# or specific columns using a list of column indicies:

e = grades[:,[0,2]]
#print(e)
#output = [[ 87  70] 
#          [100  90] 
#          [ 94  90] 
#          [100  82]]







'''
Use Numpy random-number generation to create an array of twelve random grades in the range
60 through 100, then reshape the result into a 3-by-4 array. Calculate the average of all the
grades, the averages of the grades for each test, and the averages of the grades for each student.
'''

grades = np.random.randint(60,101,12).reshape(3,4)
#print(grades)
#output = [[65 88 64 66] 
#          [79 78 78 81] 
#          [61 60 76 83]]

#print(grades.min())
#output = 60

#print(grades.mean(axis=0))
#output = [68.33333333 75.33333333 72.66666667 76.66666667]

#print(grades.mean(axis=1))
#output = [70.75 79.   70.  ]



#Shallow copies (returns a new array object that is a view of the original array NOT CREATING A NEW ARRAY)
numbers = np.arange(1,6)
#array([1, 2, 3, 4, 5])

numbers2 = numbers.view()
#array([1, 2, 3, 4, 5])

numbers[1] *= 10
#array([1, 20, 3, 4, 5])
#print(numbers2)
#array([1, 20, 3, 4, 5])

#Similarly, changing a value in the view also changes that value in the original array:
numbers2[1] /= 10
#array([1, 2, 3, 4, 5])
#print(numbers)
#array([1, 2, 3, 4, 5])


#Slice views
#Slices also create views. Let's make numbers2 a slice that views only the first three elements of numbers:
numbers2 = numbers[0:3]
#To verify it is a view, lets modigy an elemtn in the original array and see the view array
numbers[1] *= 20
#print(numbers2)
#array([ 1, 40, 3])


#Deep copies (copy)
#The array method copy returns a NEW ARRAY OBJECT with a deep copy of the original array
numbers = np.arange(1,6)
numbers2 = numbers.copy()

#To prove that numbers2 has a separate copy of the data in numbers, lets modify an elemtn in numbers, then display both arrays:

numbers[1] *= 10
#print(numbers)
# array([ 1, 20, 3, 4, 5])
#print(numbers2)
# array([ 1, 2, 3, 4, 5])


'''
The array methods require and resize both enable you to change an array's dimensions. Method reshape returns a view (shallow copy) of 
the original array with the new dimensions. It does not modify the original array:
'''

grades = np.array([[87, 96, 79], [100, 87, 90]])

a = grades.reshape(1,6)
#print(a)
#output = [[ 87  96  79 100  87  90]]
#print(grades)
#output = [[ 87  96  79]
#          [100  87  90]]

b = grades.resize(1,6)
#print(grades)
#output = [[ 87  96  79 100  87  90]]



#################################################
# Both methods below make a 1-dimensional array #
#################################################

#Method flatten deep copies the original array's data:
flattened = grades.flatten()

#Alternatively, Method ravel produces a view (shallow copy) of the original array, which shares the grades array's data:
raveled = grades.ravel()

#Confirm that they share the same data
raveled[0] = 100
raveled[5] = 99

#print(grades)
#output = [[100  96  79 100  87  99]]


#You can quickly transpose an array's rows and columns - that is "flip" the array, so the rows become the columns and vice versa
#The T attribute returns a transposed view (shallow copy) of the array.

transposed = grades.T
#print(transposed)


################################################
#              Combining Arrays                #
################################################



#HSTACK (Horizontal stacking)
#Let's assume grades2 represents three additional exam grades for the two students in the grades array

grades = np.array([[87, 96, 79], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades, grades2))

#new array (DEEP COPY)
#print(h_grades)
#output = [[ 87  96  79  94  77  90]
#          [100  87  90 100  81  82]]
#old array is NOT affected
#print(grades)
#output = [[ 87  96  79]
#          [100  87  90]]


#VSTACK (Vertical stacking)
#Let's assume that grades2 represents two more students' grades on three exams.

v_grades = np.vstack((grades, grades2))
#print(v_grades)
#output = [[ 87  96  79]
#          [100  87  90]
#          [ 94  77  90]
#          [100  81  82]]













