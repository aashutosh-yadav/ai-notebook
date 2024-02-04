#usr/bin/env python3

import sklearn
import numpy as np
import pandas as pd

#this is the linear data to test the equation .

x = 2*np.random.rand(100 ,1)
y = 4 + 3* x + np.random.randn(100,1) #added a littlbit of noise(gaussian noise)

print(x)
print("this is the seperate line ")
print(y)

#computing the theata

x_b = np.c_[np.ones((100, 1)), x]
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
print("this is the theta", theta_best)
len(x_b)

#the output y
x_new = np.array([[0] , [2]])
x_new_b = np.c_[np.ones((2,1)),x_new]
y_predict = x_new_b.dot(theta_best)
print(y_predict)


#gradient descent
eta = 0.1 # learning rate
n_iterations = 1000
m = 100
theta = np.random.randn(2,1) # random initialization
for iteration in range(n_iterations):
 gradients = 2/m * x_b.T.dot(x_b.dot(theta) - y)
 theta = theta - eta * gradients

print(theta)


