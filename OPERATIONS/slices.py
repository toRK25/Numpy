#numpy operations

import numpy as np

#slicing

arr=np.arange(15)
print("BASIC SLICING ",arr[2:13])

arr1=np.array([1,2,34,4,4,5,6,2,6,4,21,34,5,5,24,42,42,5,9,8,5,3,7,6,4])
print("SLICING WITH STEP ",arr1[2:25:3])
print("NEGATIVE INDEXING ",arr1[-13])

# IN PYTHON IT ALWAYS STARTS FROM 0 WHEN 1 WRITE ARR(1,4) IT MEANS 0th row and 3rd column 

#matric slicing

arr2=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(arr2)
print("SLICING A MATRIX ",arr2[1,2])

#to print entire row
print("3rd ROW ",arr2[2])

#to print column
print("2nd COLUMN ",arr2[:,1])