import numpy as np

#adding

arr1=np.array([2,4,5])
arr2=np.array([5,7,2])

add=arr1+arr2
print("Addition of two arrays:", add)

#combined(concatinate)

comb= np.concatenate((arr1, arr2))
print("Combined arrays:", comb)

#add new row block in array

arr3=np.array([[2,3,4],[5,4,1]])
newarr=np.array([5,8,6])

newblock=np.vstack((arr3,newarr))
print("New Row block added to the array:\n", newblock)
print("old array:\n", arr3)

#adding new column block in array
newarr1=np.array([[5],[8]])
newcol=np.hstack((arr3,newarr1))
print("New Column block added to the array:\n", newcol)

#delete
#value at 2nd place deleted
delte=np.delete(arr1,2)
print("Array after deleting element at index 2:", delte)