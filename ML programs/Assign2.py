import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv(r'D:\ML_CSV\ml.csv')
print(data)

print(data['Country'].value_counts())
print(data['Purchased'].value_counts())

ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform='pandas')
ohe_Country = ohe.fit_transform(data[['Country']])
ohe_Purchased = ohe.fit_transform(data[['Purchased']])

data = pd.concat([ohe_Country, ohe_Purchased, data], axis=1).drop(columns=['Country', 'Purchased'])

print(data)

np.set_printoptions(suppress=True)

knnimputer = KNNImputer(n_neighbors=2)
imputed_data = knnimputer.fit_transform(data)
print(imputed_data)


