import numpy as np

a=np.array([2,5,7,9])                                                                                                                                
print('a=')                                                                                                                                          
print(a)                                                                                                                                             
print(type(a))                                                                                                                                              
                                                                                                                                                     
#multidimensional array                                                                                                                              
b= np.array([[2,5,7],[3,4,5]])                                                                                                                       
print('b=')                                                                                                                                          
print(b)                                                                                                                                             
                                                                                                                                                     
#knowing dimensions of the array                                                                                                                     
print(b.shape)                                                                                                                                       
                                                                                                                                                     
#retrieving data                                                                                                                                     
#first row                                                                                                                                           
print(b[0])                                                                                                                                          
                                                                                                                                                     
#first and second row                                                                                                                                
print(b[[0,1]])                                                                                                                                      
                                                                                                                                                     
#first to last row                                                                                                                                   
print(b[0:])                                                                                                                                         
                                                                                                                                                     
#first to second row                                                                                                                                 
print(b[0:2])                                                                                                                                        
#last one gets excluded                                                                                                                              
                                                                                                                                                     
#all rows and first col                                                                                                                              
print(b[0:,0])              
