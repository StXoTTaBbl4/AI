import numpy
import numpy as np
import pandas.core.frame


def entropy(labels: numpy.ndarray) -> float:
    # Получаем уникальные метки классов и их количество
    _, counts = np.unique(labels, return_counts=True)

    # Вычисляем вероятности появления каждого класса
    probabilities = counts / len(labels)

    # Вычисляем энтропию
    entropy_value = -np.sum(probabilities * np.log2(probabilities))

    return entropy_value


def entropy_info(dataframe: pandas.core.frame.DataFrame, property_name, target_class_name='CATEGORICAL') -> float:
    # print(f'Property name {property_name}================================')
    # print(dataframe)
    attribute = np.asarray(dataframe[property_name])
    v, c = np.unique(attribute, return_counts=True)
    # print(f'Vals {v}\n{c}')
    _sum = 0
    for i in range(len(v)):
        buff = dataframe.drop(dataframe[dataframe[property_name] != v[i]].index, inplace=False)
        # print(buff)
        _sum += c[i]/len(attribute)*entropy(np.asarray(buff[target_class_name]))
    return _sum


def gain(entropy_of_target_class: float, entropy_of_properties: dict) -> dict:
    result = {}
    for k in entropy_of_properties.keys():
        result[k] = entropy_of_target_class - entropy_of_properties[k]
    return result


def split_info(labels: numpy.ndarray) -> float:
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return -sum(probabilities*np.log2(probabilities))


def gain_ratio(gains: dict, split_infos: dict) -> dict:
    result = {}
    for k in gains.keys():
        result[k] = gains[k]/split_infos[k]
    return result
