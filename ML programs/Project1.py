import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r'D:\ML_CSV\Customer_Call_List.csv')


label_encoder = LabelEncoder()

data['Paying_Customer'] = label_encoder.fit_transform(data['Paying_Customer'])
data['Do_Not_Contact'] = label_encoder.fit_transform(data['Do_Not_Contact'])
data['Not_Useful_Column'] = label_encoder.fit_transform(data['Not_Useful_Column'])

data['Paying_Customer'] = data['Paying_Customer'].replace({2:np.nan})
data['Do_Not_Contact'] = data['Do_Not_Contact'].replace({2:np.nan})

knnimputer = KNNImputer()
imputed_data = knnimputer.fit_transform(data.iloc[:, 1:3])
imputed_df = pd.DataFrame(imputed_data)

data[['Paying_Customer', 'Do_Not_Contact']] = imputed_df.astype(int)

print(data)


