import numpy as np


def get_weights_matrix(X, Y):
    """
    Вычисляет коэффициенты линейной регрессии матричным методом
    :param X: Матрица независимых коэффициентов (получена с помощью utility.get_normalized_matrix(df, features))
    :param Y: Массив зависимых переменных
    :return:
    """
    return np.linalg.inv(X.T @ X) @ X.T @ Y


# def get_weights_scalar(X, Y):
#     n = len(X)
#     width = len(X[0])
#     A = []
#     B = [sum(Y)]
#
#     for i in range(width):
#         B.append(sum(Y * X[:, i]))
#
#     A.append([])
#     tmp = A[0]
#     tmp.append(n)
#     for i in range(width):
#         tmp.append(sum(X[:, i]))
#
#     for i in range(width):
#         A.append([])
#         tmp = A[i + 1]
#         tmp.append(sum(X[:, i]))
#         for j in range(width):
#             tmp.append(sum(X[:, i] * X[:, j]))
#
#     return np.linalg.solve(A, B)


def r_squared(y_true, y_pred):
    """
    Вычисляет коэффициент детерминации
    :param y_true: Массив истинных значений
    :param y_pred: Массив предсказанных значений
    :return: Значение коэффициента детерминации
    """
    mean_y_true = np.mean(y_true)
    total_sum_squares = np.sum((y_true - mean_y_true) ** 2)
    residual_sum_squares = np.sum((y_true - y_pred) ** 2)

    r2 = 1 - (residual_sum_squares / total_sum_squares)
    return r2


def test(weights, X):
    """
    Предсказывает значения, используя коэффициенты.
    :param weights: Коэффициенты линейной регрессии в виде одномерного вектор-столбца.
    :param X: Массив независимых переменных
    :return: одномерный массив предсказанных значений
    """
    y_pred = []
    for i in range(len(X)):
        y_pred.append(sum(X[i] @ weights))
    return y_pred
