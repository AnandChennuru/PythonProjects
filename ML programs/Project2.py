import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'D:\\ML_CSV\Ice_Cream.csv')
print(df)
 
plt.xlabel('Temperature')
plt.ylabel('Revenue')
plt.scatter(df[['Temperature']], df[['Revenue']])
plt.show()

# Seperating independant(X) and dependant(y) variables
x = df[['Temperature']]
y = df[['Revenue']]

# Splitting data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

# Applying Linear Regression Algorithm
lr = LinearRegression()

# Training model using fit()
lr.fit(x_train, y_train)

lr_score = lr.score(x_test, y_test)

print(lr.predict([[22.4]]))

# Plotting with best fit line
plt.xlabel('Temperature')
plt.ylabel('Revenue')
plt.scatter(df[['Temperature']], df[['Revenue']])
plt.plot(x_train, lr.predict(x_train), color='red')
plt.show()