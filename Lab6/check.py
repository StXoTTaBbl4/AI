import numpy as np
import pandas as pd

import c45
nar = np.array([[">=9","Yes"],[">=8","Yes"],[">=9","No"],["<8","No"],[">=8","Yes"],[">=9","Yes"],["<8","No"],[">=9","Yes"],[">=8","Yes"],[">=8","Yes"]])
dataframe = pd.DataFrame(nar, columns=['1', 'CATEGORICAL'])
Y = dataframe['CATEGORICAL']
X = dataframe.drop(['CATEGORICAL'], axis=1)

# entropy = c45.entropy(np.asarray(Y))
# print(f'Энтропия предсказываемого признака: {entropy}')
#
# entropy_info = {}
# for name in X.columns.values:
#     entropy_info[name] = c45.entropy_info(pd.DataFrame(X[name]).join(Y), name)
# print(f'Entropy info признаков\n{entropy_info}')
#
# information_gain = c45.gain(entropy, entropy_info)
# print(f'Information gain признаков: \n{information_gain}')
#
# split_info = {}
# for name in X.columns.values:
#     split_info[name] = c45.split_info(np.asarray(X[name]))
# print(f'Split info признаков\n{split_info}')
#
# gain_ratio = c45.gain_ratio(information_gain, split_info)
# print(f'Gain ratio признаков:\n{gain_ratio}')
