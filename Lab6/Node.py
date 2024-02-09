import numpy as np
import pandas.core.frame
import pandas as pd

import c45
import utility


class Node:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.max_gain_key = None
        self.max_gain_val = None
        self.criteria = []
        self.sub_nodes = {}
        self.end_node = False
        self.predicted_class = None

    def __str__(self):
        print(f'Property: {self.max_gain_key}, criteria: {self.criteria}, children_nodes: {self.sub_nodes}')

    def get_best_gain_ratio_pair(self, x_train: pandas.core.frame.DataFrame, y_train: pandas.core.frame.DataFrame):
        entropy = c45.entropy(np.asarray(y_train))
        # print(f'Энтропия предсказываемого признака: {entropy}')

        entropy_info = {}
        for name in x_train.columns.values:
            entropy_info[name] = c45.entropy_info(pd.DataFrame(x_train[name]).join(y_train), name)
        # print(f'Entropy info признаков\n{entropy_info}')

        information_gain = c45.gain(entropy, entropy_info)
        # print(f'Information gain признаков: \n{information_gain}')

        split_info = {}
        for name in x_train.columns.values:
            split_info[name] = c45.split_info(np.asarray(x_train[name]))
        # print(f'Split info признаков\n{split_info}')

        gain_ratio = c45.gain_ratio(information_gain, split_info)
        # print(f'Gain ratio признаков:\n{gain_ratio}')

        self.max_gain_key, self.max_gain_val = utility.get_max_from_dict(gain_ratio)
        # print(f'mk: {self.max_gain_key}, mv: {self.max_gain_val}')

    def proceed(self, X: pandas.core.frame.DataFrame, Y:  pandas.core.frame.DataFrame):
        self.get_best_gain_ratio_pair(X, Y)
        print(f"We are in {self.max_gain_key}")
        split = pd.DataFrame(X[self.max_gain_key]).join(Y)
        un, _ = np.unique(X[self.max_gain_key], return_counts=True)
        for u in un:
            buff = split.drop(split[split[self.max_gain_key] != u].index, inplace=False)
            _, count = np.unique(buff['CATEGORICAL'], return_counts=True)
            print(buff)
            print(count)
            if len(count) != 1:
                print(f'dropped')
                cc = X.drop([self.max_gain_key], inplace=False, axis=1)
                if not cc.empty:
                    n = Node(cc, Y)
                    n.end_node = False
                    n.proceed(n.X, n.Y)
            else:
                n = Node(None, None)
                n.end_node = True
                n.criteria.append(u)
                n.predicted_class = count[0]
                self.sub_nodes[u] = n
                return

        # split = pd.DataFrame(X[self.max_gain_key]).join(Y)
        # val, count = np.unique(X, return_counts=True)
        # print(f'Unique vars: {val}')
        # for v in val:
        #     print(f'    Working with {v} from {self.max_gain_key}')
        #     buff = split.drop(split[split[self.max_gain_key] != v].index, inplace=False)
        #     cls, c = np.unique(np.asarray(buff['CATEGORICAL']), return_counts=True)
        #     if len(c) == 1:
        #         print(f'        Var {v} belongs to a end_node!')
        #         n = Node(None, None)
        #         n.end_node = True
        #         n.criteria.append(v)
        #         n.predicted_class = cls[0]
        #         self.sub_nodes[v] = n
        #     else:
        #         print(f'        Var {v} belongs to a sub_node!')
        #         buff = X.drop([self.max_gain_key], inplace=False, axis=1)
        #         # print(f'sub_node X:{buff}')
        #         if not buff.empty:
        #             n = Node(buff, Y)
        #             n.end_node = False
        #             n.proceed(n.X, n.Y)
        #
        # # print(self.sub_nodes)

