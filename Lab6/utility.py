import sys

import numpy as np


def classify(dataframe, col_name, step=2):
    classify_by = np.asarray(dataframe[col_name])
    classes = []
    for c in classify_by:
        if c >= step * 2:
            classes.append('good')
            # classes.append(3)
        # elif step <= c < step*2:
        #     classes.append('ok')
        #     # classes.append(2)
        else:
            classes.append('bad')
            # classes.append(1)
    dataframe.insert(len(dataframe.columns), 'CATEGORICAL', classes)
    return dataframe


def split_data(X, Y, train_size=0.8, random_state=42):
    """
    Разбивает данные на тестовую и тренировочную части.
    :param X: Независимые переменные.
    :param Y: Зависимая переменная.
    :param train_size: Объем тренировочных данных 0<x<1.
    :param random_state: Для перемешивания данных.
    :return: x_train, y_train, x_test, y_test
    """
    x_train = X.sample(frac=train_size, random_state=random_state)
    x_test = X.drop(x_train.index)

    y_train = Y.sample(frac=train_size, random_state=random_state)
    y_test = Y.drop(y_train.index)
    return x_train, y_train, x_test, y_test


def get_max_from_dict(d: dict):
    _max = sys.float_info.min
    key = None
    for k in d.keys():
        if d[k] > _max:
            _max = d[k]
            key = k
    return key, _max
