#!/usr/bin/python3
import numpy as np
from random import randint

x=int(input('Enter the number of rows: '))  
y=int(input('Enter the number of cols: '))

arr=np.random.randint(100,size=(x,y))     #Inserting random integers in range 1-100 in an array
print('Required array is: ',arr)

np.savetxt('reqarr.txt',arr)              #Saving the array to a file
np.loadtxt('reqarr.txt')
