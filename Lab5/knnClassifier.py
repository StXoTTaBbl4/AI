import numpy as np


def euclidean_distance(p1, p2):
    return np.sum((p1 - p2) ** 2)


def get_neighbors(x_train, y_train, x_test_chosen, k):
    distances = []
    for i in range(len(x_train)):
        distances.append((y_train[i], euclidean_distance(x_train[i], x_test_chosen)))
    distances.sort(key=lambda student: student[1])
    # print(distances)

    neighbors = []
    for i in range(k):
        neighbors.append(distances[i])
    # print(f' neighbors for {x_test_chosen} \n{neighbors}')
    return neighbors


def predict(neighbors):
    c = {}
    for n in neighbors:
        if n[0] in c:
            c[n[0]] += 1
        else:
            c[n[0]] = 1
    max_val = max(c.values())
    for k in c:
        if c[k] == max_val:
            return k


def test(x_train, y_train, x_test, k):
    if k > len(x_train):
        print(f'k больше чем кол-во тренировочных данных: \n k={k}, len(data)={len(x_train)}')
        return None
    predicted = []
    for i in range(len(x_test)):
        predicted.append(
            predict(
                get_neighbors(x_train, y_train, x_test[i], k)))
    return predicted
