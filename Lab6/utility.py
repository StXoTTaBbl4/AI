import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


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


def split_data(X: pd.DataFrame, Y: pd.DataFrame, train_size=0.8, random_state=42):
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


def get_fntp(real: list, pred: list, positive: str, negative: str):
    tp, tn, fp, fn = 0, 0, 0, 0
    for i in range(len(real)):
        if pred[i] == positive:
            if real[i] == positive:
                tp += 1
            else:
                fp += 1
        if pred[i] == negative:
            if real[i] == positive:
                fn += 1
            else:
                tn += 1
    return tp, tn, fp, fn


def accuracy(tp, tn, fp, fn):
    return (tp + tn) / (tp + fn + tn + fp)


def precision(tp, fp):
    try:
        return tp / (fp + tp)
    except ZeroDivisionError:
        return 0


def recall(tp, fn):
    return tp / (fn + tp)


def calculate_proba(X_values, root, depth=0):
    # Для каждой выборки в тестовом наборе ваша модель должна выводить оценку или набор оценок,
    # представляющих вероятность принадлежности к каждому классу
    if root.class_name is not None:
        return 1 / depth

    if X_values[root.feature] < root.div_value:
        return calculate_proba(X_values, root.left, depth + 1)
    else:
        return calculate_proba(X_values, root.right, depth + 1)


def calculate_probas(X, tree):
    probas = []
    for ind in range(X.shape[0]):
        probas.append(calculate_proba(X.iloc[ind].to_dict(), tree))

    return probas
