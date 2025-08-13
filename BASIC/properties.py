# NUMPY ARRAY PROPERTIES
import numpy as np

arr=np.array([[[1,2,3],[4,5,6]],[[7,6,54],[43545,45,45]]])
print("TENSOR : \n",arr)
print("SHAPE \n",arr.shape)
print("DIMENSION \n",arr.ndim)
print("size \n",arr.size)
print("DATA TYPE \n",arr.dtype)
print("ITEM SIZE \n",arr.itemsize)
print("BYTES \n",arr.nbytes)
print("STRIDES \n",arr.strides)
print("REAL \n",arr.real)
print("IMAGINARY \n",arr.imag)

# ARRAY RESHAPING

arr=np.arange(12)
print("ARRAY : \n",arr)

res=arr.reshape((6,2))
print("RESHAPED ARRAY : \n", res)

flat=res.flatten()
print("FLATTENED ARRAY : \n", flat)

ravel=res.ravel()
print("RAVELED ARRAY : \n", ravel)

# WHAT IS THE DIFFERENCE BETWEEM RAVEL AND FLATTEN WHEN BOTH GIVE THE SAME OUTPUT?
# Ravel returns a flattened array and does not create a copy if not necessary, while flatten always returns a copy.