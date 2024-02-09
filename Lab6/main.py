import math
import numbers
from Node import Node

import pandas as pd
import numpy as np

import c45
import utility

pd.set_option('display.max_columns', None)
dataframe = pd.read_csv('data.csv')
dataframe.replace('', np.nan, inplace=True)
dataframe.dropna()

dataframe = utility.classify(dataframe, 'GRADE', 2)
# print(dataframe.head())
dataframe = dataframe.drop(['STUDENT ID'], axis=1)
Y = dataframe['CATEGORICAL']
X = dataframe.drop(['CATEGORICAL'], axis=1)

drop_count = len(X.columns) - int(math.sqrt(len(X.columns)))
columns_to_drop = np.random.choice(X.columns.values, size=drop_count, replace=False)
X = X.drop(columns_to_drop, axis=1)

x_train, y_train, x_test, y_test = utility.split_data(X, Y, 0.8, 42)


n = Node(x_train, y_train)
n.proceed(x_train, y_train)
print(n)
print('ff')

