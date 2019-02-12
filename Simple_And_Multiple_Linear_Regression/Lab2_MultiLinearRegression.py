#BRYAN BEIDER
#Intro Machine Learning
#LAB 2

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

print('LOAD AND VISIALIZE THE DATA')#------------------
#------------READ DATA ------------
names =[
    't',                                  # Time (secs)
    'q1', 'q2', 'q3',                     # Joint angle   (rads)
    'dq1', 'dq2', 'dq3',                  # Joint velocity (rads/sec)
    'I1', 'I2', 'I3',                     # Motor current (A)
    'eps21', 'eps22', 'eps31', 'eps32',   # Strain gauge measurements ($\mu$m /m )
    'ddq1', 'ddq2', 'ddq3'                # Joint accelerations (rad/sec^2)
]

df = pd.read_csv('exp1.txt', header=None,index_col=0,names=names,na_values='?')

print(df.head(6))

#------------Plot Current 2nd Joint -----------
y = np.array(df['I2'])
t = np.array(df.index.values)
plt.plot(t,y,'ob')
plt.xlabel('time')
plt.ylabel('Current 2nd Joint')
plt.grid(True)

#-----------Define output and attributes -----

ytrain = y
Xtrain = np.array(df[['q2','dq2','eps21', 'eps22', 'eps31', 'eps32','ddq2']])



print('FIT A LINEAR MODEL')#-----------------------
regr = linear_model.LinearRegression()
regr.fit(Xtrain,ytrain)
#print('PRINT COEFFICIENTS = ',regr.coef)

y_tr_pred = regr.predict(Xtrain)
RSS_tr = np.mean((y_tr_pred-ytrain)**2)/(np.std(ytrain)**2)
print("RSS per sample = {0:f}".format(RSS_tr))

plt.plot(t, y_tr_pred,'or')
plt.ylabel('Predicted and Actual Current')
plt.grid(True)



print('Measure the Fit on an Indepdent Dataset')#-----------------------------
df2 = pd.read_csv('exp2.txt', header=None,index_col=0,names=names,na_values='?')


ytest = np.array(df2['I2'])
Xtest = np.array(df2[['q2','dq2','eps21', 'eps22', 'eps31', 'eps32','ddq2']])
t2 = np.array(df2.index.values)
y_test_pred = regr.predict(Xtest)
RSS_test = np.mean((y_test_pred-ytest)**2)/(np.std(ytest)**2)
print("RSS per sample = {0:f}".format(RSS_test))

plt.figure(2)
plt.plot(t2,ytest,'ob',t2,y_test_pred,'or')
plt.ylabel('Predicted and Actual Current')
plt.grid(True)
plt.show()
