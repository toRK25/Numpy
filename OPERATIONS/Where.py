import numpy as np

arr=np.array([2,5,7,1,3,4,9,7,8,3,1,5,7,0])

where=np.where(arr>6)
print("Indices where elements are greater than 6:", arr[where])

#conditional selection like if elif else

cond=np.where(arr>3,arr*3,arr==3)
print("Conditional selection (if > 3, multiply by 3; else keep original):", cond)