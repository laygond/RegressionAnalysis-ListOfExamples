# RegressionAnalysis-ListOfExamples
Intro to Machine Learning and Optimization. COMPENDIUM of the different types of regression techniques used in Machine Learning and Optimization as well as guidance to what libraries can be used in Python.

## What is Regression Analysis?
Regression analysis is a form of predictive modelling technique which investigates the relationship among variables. 

A regression model relates Y to X and β <br> 
Y ≈ f ( X , β ) 

where depending on the field: <br>
- X is known as the **independent variable**, predictor variable, regressor, covariate, controlled variable, manipulated variable, explanatory variable, exposure variable, risk factor, feature, or input variable.
- Y is known as the **dependent variable**, response variable, regressand, criterion, predicted variable, target variable, measured variable, explained variable, experimental variable, responding variable, outcome variable, label, or output variable.
- β  is the unknown parameters.

If Y = f(X,β) = Xβ we say the regression is linear otherwise it is non-linear. If Y and β are matrices then we call the regression multivariate. If Y and β are one dimensional vectors then the regression is univariate and this is generally assumed unless multivariate is specified.

NOTE: Every regression can be stated as an optimization problem and therefore might have diffrent methods for solving it.

## Links to Regression Examples
- Linear (Univariate) Regressions **y = Xβ**
    - Simple and Multiple linear regression
    - Polynomial Regression    
    - Ridge Regression
    - Lasso Regression
    - ElasticNet Regression
    - Logistic Regression

## Essential Libraries for Machine Learning in Python
The following is a summary of libraries that will be used throughout the REPO. 

- **Scikit-learn** is one the most popular libraries for working with classical ML algorithms. It builds on three basic libraries of Python: NumPy, SciPy, and Matplotlib.  It supports many supervised and unsupervised learning algorithms. With Scikit-learn you can peform classification, regression, clustering, dimensionality reduction, model selection, or feature extraction.

- **Pandas** is a very popular library used for data extraction. Pandas can easily fetch data from different sources like SQL databases, CSV, Excel, JSON files and manipulate the data into high-level data structures which are simple to use as well as intuitive.

- **Matplotlib** for data visualization is a standard Python library used by every data scientist. In addition, Matplotlib allows to export to common graphic formats like PDF, SVG, JPG, PNG, BMP, GIF, etc.

As an editor I recommend using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#) since all examples are saved as .ipynb file extensions.

NOTE: For a novice in ML, Scikit-learn is a more-than-sufficient tool to work with until you start implementing more complex algorithms. (Tensorflow, Pytorch, or Caffe for Deep Learning).

## Bibliography
- https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/
- https://medium.freecodecamp.org/essential-libraries-for-machine-learning-in-python-82a9ada57aeb
- https://scikit-learn.org/stable/modules/linear_model.html
- https://www.datascience.com/blog/7-methods-to-fit-linear-model-python