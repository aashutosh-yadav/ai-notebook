'''svm can perform non liner regression as well as linear regerssion.
But what is a kernal trick ?

now here this is like a very basic implementation means it is the like the classification for the point with svm 
,it will tell us where the ponint lies .

now suppose we havs two arrays of namely x and b , from which x has two points which means the plane is 
two dimensional and we have parameter b which has the parameter b_1 and b_0 
if out x points satifies the equation then the the equation is equal to zero 
β0 + β1X1 + β2X2 = 0 -> like this equation .
'''
import numpy as np
def fun(x ,b, b_0):
    y = np.dot(x,b) + b_0
    print(y)
    if y > 0:
        print("is in the right side of the plane ")
    else :
        print("is in the left side of the plane ")

    
x = np.array([1, 2]) 
b = np.array([1, 2])  
b_0 = 1

ans = fun(x , b , b_0)
print(ans)
