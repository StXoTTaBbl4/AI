import numpy as np


def split_data(x, y, test_size=0.2, random_state=1707):
    """
    Разбивает данные на тестовую и тренировочную.
    :param x: Независимые переменные.
    :param y: Зависимая переменная.
    :param test_size: Объем тестовых данных 0<x<1.
    :param random_state: Для перемешивания данных.
    :return: x_train, y_train, x_test, y_test
    """
    np.random.seed(random_state)  # set the seed for reproducible results
    indices = np.random.permutation(len(x))  # shuffling the indices
    data_test_size = int(x.shape[0] * test_size)  # Get the test size

    # Separating the Independent and Dependent features into the Train and Test Set
    train_indices = indices[data_test_size:]
    test_indices = indices[:data_test_size]
    x_train = x[train_indices]
    y_train = y[train_indices]
    x_test = x[test_indices]
    y_test = y[test_indices]
    return x_train, y_train, x_test, y_test


def create_normalized_matrix(df, features):
    """
    Метод для создания матрицы, которая будет использована для вычисления коэффициентов линейной регрессии.
    :param df: Файл pd.read...
    :param features: Массив названий столбцов, которые являются независимыми переменными.
    :return: Матрица с нормализованными значениями.
    """
    columns = []
    for i in range(len(features)):
        x = np.asarray(df[features[i]].values.tolist())
        x = (x - int(np.min(x))) / (np.max(x) - np.min(x))
        columns.append(x.reshape(-1, 1))
    columns.insert(0, np.ones((columns[0].shape[0], 1)))
    return np.concatenate(columns, axis=1)


def get_list_without_feature(_list, feature):
    """
     Это костыль. Я в душе не понимаю что за хрень с листом, но внутри цикла он не восстанавливается, так что так.
    :param _list: Исходный лист
    :param feature: Элемент который надо убрать
    :return: Лист без элемента
    """
    new_list = []
    for i in _list:
        if i != feature:
            new_list.append(i)
    return new_list
