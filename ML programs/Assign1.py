import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv(r'D:\ML_CSV\house.csv')
print("Original Data")
print(data)

scaler = MinMaxScaler()
scaler.fit(data)

new_data = scaler.transform(data)
print("New Data")
print(new_data)