import numpy as np
print("Creating a numpy array of 8x2 with numbers between 100 to 200 and increasing with 5:")

arr=np.arange(100,180,5)
arr=arr.reshape(8,2)

print(arr)
