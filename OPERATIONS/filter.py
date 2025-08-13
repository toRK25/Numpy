import numpy as np

arr=np.array([1,4,7,8,4,6,7,2,6,4,9,7,6,3])
even=arr[arr%2==0]
print("EVEN NUMBERS ", even)

#filters with conditions
#1
mask=arr>5
print("MASKED ARRAY ", arr[mask])
print("SORTED MASKED ARRAY ", np.sort(arr[mask]))

#2
INDEX=[2,4,0]
print("INDEXED ARRAY ", arr[INDEX])
