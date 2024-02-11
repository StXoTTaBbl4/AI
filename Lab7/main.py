import math

import numpy as np
import pandas as pd
import pyarrow
from prettytable import PrettyTable

import logical_regression
import utility

pd.set_option('display.max_columns', None)
dataframe = pd.read_csv('diabetes.csv')
dataframe.replace('', np.nan, inplace=True)
dataframe.dropna()
Y = dataframe['Outcome']
X = utility.normalize(dataframe.drop('Outcome', axis=1))

x_train, y_train, x_test, y_test = utility.split_data(X, Y, 0.8, 42)
table = PrettyTable()
table.field_names = ['method', 'iterations', 'learning rate', 'accuracy', 'precision', 'recall', 'f1']

it = [50, 500, 2000]
rt = [0.01, 0.1, 0.5]
top_f1 = -1
top_data = []
for i in it:
    # Gradient
    for r in rt:
        buff_c, losses = logical_regression.gradient_descent(x_train, y_train, i, r)
        buff_pred = logical_regression.predict(x_test, buff_c)
        scores = utility.calculate_metrics(buff_pred, y_test)
        data = ['Gradient', i, r, scores['accuracy'], scores['precision'], scores['recall'], scores['f1']]
        table.add_row(data)
        if scores['f1'] > top_f1:
            top_f1 = scores['f1']
            top_data = data
# Newton
    buff_c, losses = logical_regression.newton_optimization(x_train, y_train, i)
    buff_pred = logical_regression.predict(x_test, buff_c)
    scores = utility.calculate_metrics(buff_pred, y_test)
    data = ['Newton', i, '-', scores['accuracy'], scores['precision'], scores['recall'], scores['f1']]
    table.add_row(data)
    if scores['f1'] > top_f1:
        top_f1 = scores['f1']
        top_data = data

print(table)
table.clear()
table.field_names = ['method', 'iterations', 'learning rate', 'accuracy', 'precision', 'recall', 'f1']
table.add_row(top_data)
print(f'Best try: \n{table}')