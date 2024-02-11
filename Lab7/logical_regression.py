import numpy as np
import pandas as pd

import utility


def sigmoid_function(val: float) -> float:
    return 1 / (1 + np.exp(-val))


# Вместо СКО
def log_loss_function(real, pred):
    return -np.mean(real * np.log(pred) + (1 - real) * np.log(1 - pred))


def newton_optimization(x_train, y_train, iterations):
    objects_num, characteristics_num = x_train.shape

    weights = np.zeros(characteristics_num)
    losses = []
    bias = 0

    for iteration in range(1, iterations + 1):

        t = x_train @ weights + bias
        #  prediction
        z = sigmoid_function(t)

        # The partial derivative of los.fun w.r.t. weight
        dw = (1 / objects_num) * x_train.T @ (z - y_train)
        # A partial derivative of los.fun w.r.t. value
        db = (1 / objects_num) * np.sum(z - y_train)
        # The second derivative
        hessian = (1 / objects_num) * (x_train.T @ ((z * (1 - z)) * x_train.T).T)

        weights -= np.linalg.inv(hessian) @ dw
        bias -= db

        if iteration % 100 == 0:
            loss = log_loss_function(y_train, z)
            losses.append(loss)
            # print(f'{iteration}) cost = {loss}')

    coeff = {'weights': weights, 'bias': bias}
    return coeff, losses


def gradient_descent(x_train, y_train, iterations=100, learning_rate=0.1):
    n_samples, n_features = x_train.shape
    weights = np.zeros(n_features)
    losses = []
    bias = 0

    for iteration in range(1, iterations + 1):

        # Corrected prob
        t = x_train @ weights + bias
        # prediction
        z = sigmoid_function(t)

        # The partial derivative of los.fun w.r.t. weight
        dw = (1 / n_samples) * x_train.T @ (z - y_train)
        # A partial derivative of los.fun w.r.t. value
        db = (1 / n_samples) * np.sum(z - y_train)

        # Correction
        weights -= learning_rate * dw
        bias -= learning_rate * db

        if iteration % 100 == 0:
            loss = log_loss_function(y_train, z)
            losses.append(loss)
            # print(f'{iteration} cost = {loss}')

    c = {'weights': weights, 'bias': bias}
    return c, losses


def predict(X_test, coeff):
    weights = coeff['weights']
    bias = coeff['bias']
    t = np.dot(X_test, weights) + bias
    z = sigmoid_function(t)
    return (z > 0.6).astype(int)


def get_metrics(pred, real):
    tp, tn, fp, fn = utility.get_fntp(pred, real, 1, 0)
    accuracy = utility.accuracy(tp, tn, fp, fn)
    precision = utility.precision(tp, fp)
    recall = utility.recall(tp, fn)
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
    return {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1}
