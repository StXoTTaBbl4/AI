import random

import numpy as np
import pandas
import pandas as pd


def normalize(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Нормализация значений(min/max)
    :param df: Dataframe с данными
    :return: Dataframe с нормализованными данными
    """
    for c_name, params in df.items():
        # mean = params.mean()
        # std = params.std()
        # ind_features[c_name] = (ind_features[c_name] - mean) / std
        minimum = min(params)
        maximum = max(params)
        diff = maximum - minimum
        df[c_name] = (df[c_name] - minimum) / diff
    return df


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


def calculate_metrics(Y_prediction, Y_test):
    TP = np.sum((Y_prediction == 1) & (Y_test == 1))
    TN = np.sum((Y_prediction == 0) & (Y_test == 0))
    FP = np.sum((Y_prediction == 1) & (Y_test == 0))
    FN = np.sum((Y_prediction == 0) & (Y_test == 1))

    accuracy = (TP + TN) / (TP + TN + FP + FN) if (TP + TN + FP + FN) != 0 else 0
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

    return {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1_score}
