#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv("Position_Salaries.csv")
dataset.head()
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

# Since the data set is really small, we are not splitting it into Training set and a test set. So we are using the whole data as training set

#Splitting the dataset into Training set and Test set
'''
from sklearn.cross_validation import train_test_split #Use  from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)
'''

# Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #We don not need to fit the sc_X object to the test set coz it is already fitted to the Training Set
"""
# We have linear Regression so that we can compare Linear Regression dataset and its predictions with Polynomial regression dataset and its predictions

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Fitting the Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 9)
X_poly = poly_reg.fit_transform(X)

# Fitting the model with LinearRegression for the Polynomial Independent variable
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

# Visualising the Linear Regression results
plt.scatter(X,y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff of emp Salary (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X,y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff of emp Salary (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#  Visualising the Polynomial Regression results with X_grid
X_grid = np.arange(min(X),max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff of emp Salary (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression 
#lin_reg.predict(X)
# So for an employee suppose we have 6.5 () then
lin_reg.predict(6.5)

# Predecting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))

'''y_pred = lin_reg_2.predict(X_poly)

plt.scatter(X,y, color = 'red')
plt.plot(X, y_pred, color = 'blue')
plt.title('Truth or Bluff of emp Salary (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()'''

'''
# To get Best degree for the Polynomial
rmses = []
degrees = np.arange(1, 10)
min_rmse, min_deg = 1e10, 0

for deg in degrees:

    # Train features
    poly_features = PolynomialFeatures(degree=deg, include_bias=False)
    x_poly_train = poly_features.fit_transform(X)

    # Linear regression
    poly_reg = LinearRegression()
    poly_reg.fit(x_poly_train, y)

    # Compare with test data
    from sklearn.metrics import mean_squared_error
    x_poly_test = poly_features.fit_transform(X)
    poly_predict = poly_reg.predict(x_poly_test)
    poly_mse = mean_squared_error(y, poly_predict)
    poly_rmse = np.sqrt(poly_mse)
    rmses.append(poly_rmse)

    # Cross-validation of degree
    if min_rmse > poly_rmse:
        min_rmse = poly_rmse
        min_deg = deg

# Plot and present results
print('Best degree {} with RMSE {}'.format(min_deg, min_rmse))
'''