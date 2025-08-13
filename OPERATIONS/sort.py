import numpy as np

arr=np.array([1,8,6,4,89,3,3,4,7,1,9,65,1,5,8,0,5,3,2,6,8,9])
print("UNSORTED ARRAY ", arr)
print("SORTED ARRAY ", np.sort(arr ))

#SORT ROW AND COLUMN
arr1=np.array([[1,2,3],[7,3,9],[2,7,4],[6,2,5]])
print("SORT ONLY columns : ", np.sort(arr1, axis =0))
print("SORT ONLY rows : ", np.sort(arr1, axis =1))