# RegressionAnalysis-ListOfExamples
Intro to Machine Learning and Optimization. COMPENDIUM of the different types of regression techniques used in Machine Learning and Optimization as well as guidance to what libraries can be used in Python.

## What is Regression Analysis?
Regression analysis is a form of predictive modelling technique which investigates the relationship among variables. 

A regression model relates $Y$ to $X$ and $Β$ <br>
<center> $Y ≈ f ( X , Β )$ </center> 

where depending on the field: <br>
- $X$ is known as the **independent variable**, predictor variable, regressor, covariate, controlled variable, manipulated variable, explanatory variable, exposure variable, risk factor, feature, or input variable.
- $Y$ is known as the **dependent variable**, response variable, regressand, criterion, predicted variable, target variable, measured variable, explained variable, experimental variable, responding variable, outcome variable, label, or output variable.
- $Β$ are the unknown parameters.

If $Y ≈ f(X,Β) = X\cdotΒ$ we say the regression is linear otherwise it remains non-linear. If $Y$ and $B$ are matrices then we call the regression multivariate. If $Y$ and $Β$ are one dimensional vectors, i.e.,  $\mathbf{y}$ and $\mathbf{β}$, then the regression is univariate and this is generally assumed unless multivariate is specified.

### Notation
To distinct vectors from matrices we will denote vectors in lower-case bold, i.e.,

$\mathbf{x} = \begin{bmatrix}
                x_1\\
                x_2\\
                \vdots\\
                x_n
\end{bmatrix}$

and matrices in upper-case bold. The transpose of a vector or matrix is indicated by a superscript $T$, i.e., $ \mathbf{x}^T$ is the transpose of $\mathbf{x}$.<br>
The notation $||\mathbf{x}||_2$ refers to the Euclidean length of vector $\mathbf{x}$, i.e,

$||\mathbf{x}||_2 = \sqrt{x_1^2 + x_2^2 +...+ x_n^2}$

The sum of squares of $\mathbf{x}$ is denoted by $||\mathbf{x}||_2^2$, i.e.,

$||\mathbf{x}||_2^2 = \displaystyle\sum_{i=1}^n x_i^2 =\mathbf{x}^T \cdot \mathbf{x}$

The 'energy' of a vector $\mathbf{x}$ refers to $||\mathbf{x}||_2^2$. <br>

In these notes, it is assumed that all vectors and matrices are real-valued. In the complex-valued case, the conjugate transpose should be used in place of the transpose, etc.

## Links to Regression Examples
- Linear (Univariate) Regressions $\mathbf{y} = X\cdot\mathbf{β}$
    - [Simple and Multiple linear regression](./Simple_And_Multiple_Linear_Regression)
    - [Polynomial Regression](./Polynomial_Regression)  
    - Ridge Regression
    - Lasso Regression
    - ElasticNet Regression
    - [Logistic Regression](./Logistic_Regression)

## Essential Libraries for Machine Learning in Python
The following is a summary of libraries that will be used throughout the REPO. 

- **Scikit-learn** is one the most popular libraries for working with classical ML algorithms. It builds on three basic libraries of Python: NumPy, SciPy, and Matplotlib.  It supports many supervised and unsupervised learning algorithms. With Scikit-learn you can peform classification, regression, clustering, dimensionality reduction, model selection, or feature extraction.

- **Pandas** is a very popular library used for data extraction. Pandas can easily fetch data from different sources like SQL databases, CSV, Excel, JSON files and manipulate the data into high-level data structures which are simple to use as well as intuitive.

- **Matplotlib** for data visualization is a standard Python library used by every data scientist. In addition, Matplotlib allows to export to common graphic formats like PDF, SVG, JPG, PNG, BMP, GIF, etc.

As an editor I recommend using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#) since all examples are saved as .ipynb file extensions.

NOTE: For pure ML operations, Scikit-learn is a more-than-sufficient tool to work with until you start implementing more complex algorithms. (Tensorflow, Pytorch, or Caffe for Deep Learning).

## Bibliography
- https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/
- https://medium.freecodecamp.org/essential-libraries-for-machine-learning-in-python-82a9ada57aeb
- https://scikit-learn.org/stable/modules/linear_model.html
- https://www.datascience.com/blog/7-methods-to-fit-linear-model-python
- http://eeweb.poly.edu/iselesni/lecture_notes/least_squares/least_squares_SP.pdf
- https://github.com/sdrangan/introml