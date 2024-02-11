import math
import NodeRe
import pandas as pd
import numpy as np

import auc_pr
import auc_roc
import utility

pd.set_option('display.max_columns', None)
dataframe = pd.read_csv('data.csv')
dataframe.replace('', np.nan, inplace=True)
dataframe.dropna()

dataframe = utility.classify(dataframe, 'GRADE', 2)
# print(dataframe.head())
dataframe = dataframe.drop(['STUDENT ID'], axis=1)
dataframe = dataframe.drop(['GRADE'], axis=1)
Y = dataframe['CATEGORICAL']
X = dataframe.drop(['CATEGORICAL'], axis=1)

drop_count = len(X.columns) - int(math.sqrt(len(X.columns)))
columns_to_drop = np.random.choice(X.columns.values, size=drop_count, replace=False)
X = X.drop(columns_to_drop, axis=1)

x_train, y_train, x_test, y_test = utility.split_data(X, Y, 0.8, 42)

tree_depth = 4
tree = NodeRe.fit(x_train, y_train, 0, tree_depth)

# NodeRe.print_tree(model)
pred = []
real = []
for ind in range(x_test.shape[0]):
    pred.append(NodeRe.predict(x_test.iloc[ind].to_dict(), tree))
    real.append(y_train.iloc[ind])

print(pred)
print(real)
tp, tn, fp, fn = utility.get_fntp(real, pred, 'good', 'bad')

print(f'Accuracy: {utility.accuracy(tp,tn, fp, fn)}\nPrecision: {utility.precision(tp, fp)}\nRecall: {utility.recall(tp, fn)}')

probas = np.sort(utility.calculate_probas(x_test, tree))
u_probas = np.unique(probas)

tprs, fprs = auc_roc.get_all_tprs_fprs(u_probas, y_test, probas)
print(f'tprs={tprs}, fprs={fprs}')
auc_roc.build_auc_roc(fprs, tprs)

auc_roc = 0
for i in range(len(fprs) - 1):
    s = (tprs[i] + tprs[i+1]) / 2 * (fprs[i + 1] - fprs[i])
    auc_roc += s
print(f'auc-roc = {abs(auc_roc)}')

ai_precision, ai_recall = auc_pr.precision_recall_curve(np.asarray(real), pred)
hm_precision, hm_recall = auc_pr.get_all_precisions_recalls(np.unique(probas), y_test, probas)

# auc_pr.build_auc_pr(ai_recall, ai_precision)
auc_pr.build_auc_pr(hm_recall, hm_precision)

# auc_pr_ai = 0
auc_pr_hm = 0
for i in range(len(fprs) - 1):
    # auc_pr_ai += (ai_precision[i] + ai_precision[i+1]) / 2 * (ai_recall[i+1] - ai_recall[i])
    auc_pr_hm += (hm_precision[i] + hm_precision[i+1]) / 2 * (hm_recall[i+1] - hm_recall[i])
# print(f'ai auc_pr = {abs(auc_pr_ai)}')
print(f'hm auc_pr = {abs(auc_pr_hm)}')