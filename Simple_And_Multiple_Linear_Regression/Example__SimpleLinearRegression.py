#BRYAN BEIDER
#Intro Machine Learning
#LAB 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#---------READING DATA------------
names =[
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
    'AGE',  'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'PRICE'
]

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
                 header=None,delim_whitespace=True,names=names,na_values='?')

print(df.head(6))

#------------MANIPULATING DATA----------
numSamples, numAttributes = df.shape
print('numSamples = ', numSamples, ' numAttributes = ', numAttributes)

#print(df.columns)
#print(df.index)
#print(df.values)

y = np.array(df['PRICE'])

yMean = np.mean(y)
numAbove40 = np.sum(y>40)
percentAbove40 = numAbove40/len(y)*100
print('The mean house price is ',yMean, ' thousands of dollars.')
print('Only ', percentAbove40, 'percent are above $40k.')


#------------VISUALIZING DATA------------
x = np.array(df['RM'])

#df2 = df1.dropna()
plt.plot(x,y,'o')
plt.xlabel('RM')
plt.ylabel('PRICE')
plt.grid(True)
#plt.show()

#-----------FITTING A SIMPLE LINEAR MODEL---------
def fit_linear(x,y):
    """
    Given vectors of data points (x,y), performs a fit for the linear model:
       yhat = beta0 + beta1*x, 
    The function returns beta0, beta1 and R_2, where R_2 is the coefficient of determination.
    """

    xm = np.mean(x)
    ym = np.mean(y)
    syy = np.mean((y-ym)**2)
    syx = np.mean((y-ym)*(x-xm))
    sxx = np.mean((x-xm)**2)
    stdy = np.sqrt(syy)
    stdx = np.sqrt(sxx)
    beta1 = syx/sxx
    beta0 = ym - beta1*xm
    ryx = syx/(stdx*stdy)
    R_2 = ryx*ryx

    return beta0, beta1, R_2

beta0,beta1,R_2 = fit_linear(x,y)
print('beta0 = ', beta0)
print('beta1 = ', beta1)
print('R_2 = ', R_2)

# Predicted regression line
xp = np.array([4,9])        #Pick two points to plot line
yp = beta1*xp + beta0
plt.plot(xp,yp,'-',linewidth=3)  # Plot the regression line on same figure
plt.show()

#----------COMPUTE COEFFICIENTS OF DETERMINATION------
def Calc_R_2(x,y):
    """
    Given vectors of data points (x,y), performs a fit for the linear model:
       yhat = beta0 + beta1*x, 
    The function returns beta0, beta1 and R_2, where R_2 is the coefficient of determination.
    """

    xm = np.mean(x)
    ym = np.mean(y)
    syy = np.mean((y-ym)**2)
    syx = np.mean((y-ym)*(x-xm))
    sxx = np.mean((x-xm)**2)
    stdy = np.sqrt(syy)
    stdx = np.sqrt(sxx)
    ryx = syx/(stdx*stdy)
    R_2 = ryx*ryx

    return R_2

R_2_Values = np.zeros(len(names)-1)             #Empty array to store R_2
for i in range(len(names)-1):
    x_for_det = np.array(df[names[i]])
    R_2_Values[i] = Calc_R_2(x_for_det,y)

npnames = np.array(names[0:len(names)-1])       #transform dictionary into np array
table = np.column_stack((npnames,R_2_Values))   #create matrix style

print('TABLE OF COEFFICIENTS OF DETERMINATION')
print(pd.DataFrame(table))                      #print panda table structure


