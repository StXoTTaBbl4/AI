import math

import numpy as np
import pandas as pd


class Node:
    def __init__(self, left=None, right=None, class_name=None, feature=None, div_value=None):
        self.left = left
        self.right = right
        self.class_name = class_name
        self.feature = feature
        self.div_value = div_value


def entropy(Y_values):
    if len(Y_values) == 0:
        return 0

    p1 = np.mean(Y_values == Y_values[0])
    p2 = 1 - p1

    if p1 == 1 or p2 == 1:
        return 0

    return -(p1 * math.log2(p1) + p2 * math.log2(p2))


def gain(X, Y):
    #  энтропия до разделения
    before = entropy(Y.values)

    #  находим уникальные значения признака и количество вхождений каждого уникального признака
    values, occurrences = np.unique(X, return_counts=True)
    total = len(Y.values)

    #  массив энтропий для того, чтобы получить взвешенную энтропию (ВЭ потом будет использоваться для определения
    #  выгоды от разделения по данному признаку)
    entropies = []
    #  пробегаюсь по всем уникальным значениям признака
    for i, value in enumerate(values):
        #  вычисляю вероятность (количество объектов с таким признаком / общее количество объектов)
        prob = occurrences[i] / total

        #  все метки данного значения X
        cur_labels = Y[X == value]

        #  высчитываю энтропию меток полученных значений меток для данного уникального значения
        tmp_entropy = prob * entropy(cur_labels.values)

        #  добавляю в массив энтропий
        entropies.append(tmp_entropy)

    return before - sum(entropies)


def fit(X: pd.DataFrame, Y: pd.DataFrame, c_depth, mx_depth):
    y_vals = np.asarray(Y)

    if len(np.unique(y_vals)) == 1:
        return Node(class_name=y_vals[0])

    if c_depth >= mx_depth:
        vals, counts = np.unique(y_vals, return_counts=True)
        return Node(class_name=vals[0] if counts[0] >= counts[1] else vals[1])

    max_gain = 0
    max_gain_key, max_gain_val = None, None

    for name in X.columns.values:
        unique = np.unique(X[name])
        for u in unique:
            left = X[name] < u
            right = X[name] >= u

            if sum(left) == 0 or sum(right) == 0:
                continue

            _gain = gain(left, Y)

            if max_gain < _gain:
                max_gain = _gain
                max_gain_key = name
                max_gain_val = u

    if max_gain == 0 or max_gain_key is None or max_gain_val is None:
        labels = np.unique(y_vals)
        label = y_vals[0]
        l1_count = 0
        for i in range(len(y_vals)):
            if y_vals[i] == label:
                l1_count += 1
        l2_count = len(y_vals) - l1_count
        return Node(class_name=labels[0] if l1_count >= l2_count else labels[1])

    left_X_ind = X[max_gain_key] < max_gain_val
    right_X_ind = X[max_gain_key] >= max_gain_val

    #  строим левое и правое деревья
    left_tree_node = fit(X[left_X_ind], Y[left_X_ind], c_depth + 1, mx_depth)
    right_tree_node = fit(X[right_X_ind], Y[right_X_ind], c_depth + 1, mx_depth)

    return Node(left=left_tree_node,
                right=right_tree_node,
                feature=max_gain_key,
                div_value=max_gain_val)


def predict(X_object_values, root):
    if root.class_name is not None:
        return root.class_name
    if X_object_values[root.feature] < root.div_value:
        return predict(X_object_values, root.left)
    else:
        return predict(X_object_values, root.right)


def print_tree(root: Node, spaces=0):
    if root.left is not None:
        print_tree(root.left, spaces + 4)
    if root.right is not None:
        print_tree(root.right, spaces + 4)

    a = f'#{root.class_name}, признак: {root.feature}, значение: {root.div_value}'
    # Не смотри сюда
    space = ""
    for i in range(spaces):
        space += " "
    print(a.replace('#', space))


