#import DATASET
import pandas as pd
from IPython.display import display
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler 
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import accuracy_score

data = pd.read_excel('session.xlsx', header=None, index_col=False, names=['x1','x2','y'])

dataset = data[['x1','x2','y']]
display(data)

minmax_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data_minmax = minmax_scaler.fit_transform(data)
print('MinMaxScaler applied on the data:\n', data_minmax)
