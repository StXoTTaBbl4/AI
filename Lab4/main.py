import sys
import numpy as np
import pandas as pd
import utility
import linear_regression


pd.set_option('display.max_columns', None)
dataframe = pd.read_csv('california_housing_train.csv')
dataframe.replace('', np.nan, inplace=True)
dataframe.dropna()
print(dataframe.info())
print(dataframe.describe())

independent_features = ["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms",
                        "population", "households", "median_income"]
dependent_feature = 'median_house_value'

# Матрица независимых переменных
X = utility.create_normalized_matrix(dataframe, independent_features)
# Зависимая переменная
Y = np.asarray(dataframe[dependent_feature].values.tolist())
Y = (Y - int(np.min(Y))) / (np.max(Y) - np.min(Y))

# Разбиение на тестовую и тренировочную части, вычисление коэффициентов
x_train, y_train, x_test, y_test = utility.split_data(X, Y, 0.2)
weights_matrix = linear_regression.get_weights_matrix(x_train, y_train).reshape(-1, 1)
pred = linear_regression.test(weights_matrix, x_test)
r2 = linear_regression.r_squared(y_test, pred)

print(f'Независимые параметры \n{independent_features}')
print(f'\nЗависимый параметр: \n{dependent_feature}')
print(f'\nКоэффициенты: \n{weights_matrix}')

r2_scores = {}

print('\nВлияние признаков:')
# Поиск наиболее влиятельного признака
for feature in independent_features:
    tmp_X = X = utility.create_normalized_matrix(dataframe, utility.get_list_without_feature(independent_features,
                                                                                             feature))
    tmp_x_train, tmp_y_train, tmp_x_test, tmp_y_test = utility.split_data(X, Y)
    tmp_weights = linear_regression.get_weights_matrix(tmp_x_train, tmp_y_train).reshape(-1, 1)
    tmp_pred = linear_regression.test(tmp_weights, tmp_x_test)

    tmp_r2 = linear_regression.r_squared(tmp_y_test, tmp_pred)
    r2_scores[feature] = (tmp_r2, tmp_r2 - r2)

max_diff = sys.float_info.min
max_diff_name = ""
for key in r2_scores.keys():
    if abs(r2_scores[key][1]) > max_diff:
        max_diff = abs(r2_scores[key][1])
        max_diff_name = key
    print(f'name: {key} r2: {r2_scores[key][0]} diff: { r2_scores[key][1]}')
print(f'\nНаибольшее влияние: {max_diff_name}')
