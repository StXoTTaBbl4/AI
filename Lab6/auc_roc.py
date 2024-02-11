from matplotlib import pyplot as plt


def get_tpr_fpr(div_value, Y_test, probas):
    predicted_values = []
    for i in range(len(probas)):
        if probas[i] >= div_value:
            predicted_values.append('good')
        else:
            predicted_values.append('bad')
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for i in range(len(Y_test)):
        if predicted_values[i] == 'good':
            if Y_test.values[i] == 'good':
                true_positive += 1
            else:
                false_positive += 1
        else:
            if Y_test.values[i] == 'good':
                false_negative += 1
            else:
                true_negative += 1

    true_positive_rate = true_positive / (true_positive + false_negative)
    false_positive_rate = false_positive / (false_positive + true_negative)
    return true_positive_rate, false_positive_rate


def get_all_tprs_fprs(div_values, Y_test, probas):
    tprs = []
    fprs = []
    for div_value in div_values:
        buff = get_tpr_fpr(div_value, Y_test, probas)
        tprs.append(buff[0])
        fprs.append(buff[1])
    return tprs, fprs


def build_auc_roc(fprs, tprs):
    plt.title('ROC curve', fontsize=12)
    plt.xlabel('FPR', fontsize=8)
    plt.ylabel('TPR', fontsize=8)
    plt.plot(fprs, tprs, 'b', fprs, fprs, 'r')
    plt.xlim(0, 1.2)
    plt.ylim(0, 1.2)
    plt.show()
