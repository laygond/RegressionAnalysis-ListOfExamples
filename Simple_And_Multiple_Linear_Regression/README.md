
Simple matrix operation perform the fastest
https://www.datascience.com/blog/7-methods-to-fit-linear-model-python

Linear Regression establishes a relationship between dependent variable (Y) and one or more independent variables (X) using a best fit straight line (also known as regression line).
It is represented by an equation Y=a+b*X + e, where a is intercept, b is slope of the line and e is error term. This equation can be used to predict the value of target variable based on given predictor variable(s).

The difference between simple linear regression and multiple linear regression is that, multiple linear regression has (>1) independent variables, whereas simple linear regression has only 1 independent variable.  Now, the question is “How do we obtain best fit line?”.



There must be linear relationship between independent and dependent variables
Multiple regression suffers from multicollinearity, autocorrelation, heteroskedasticity.
Linear Regression is very sensitive to Outliers. It can terribly affect the regression line and eventually the forecasted values.
Multicollinearity can increase the variance of the coefficient estimates and make the estimates very sensitive to minor changes in the model. The result is that the coefficient estimates are unstable
In case of multiple independent variables, we can go with forward selection, backward elimination and step wise approach for selection of most significant independent variables.