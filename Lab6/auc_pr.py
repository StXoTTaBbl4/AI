from matplotlib import pyplot as plt


def precision_recall_curve(true_labels, predicted_probs):
    thresholds = sorted(set(predicted_probs), reverse=True)
    precisions = []
    recalls = []
    for threshold in thresholds:
        predicted_labels = ['good' if prob >= threshold else 'bad' for prob in predicted_probs]
        tp = sum([1 for p, t in zip(predicted_labels, true_labels) if p == 'good' and t == 'good'])
        fp = sum([1 for p, t in zip(predicted_labels, true_labels) if p == 'good' and t == 'bad'])
        fn = sum([1 for p, t in zip(predicted_labels, true_labels) if p == 'bad' and t == 'good'])
        if tp + fp == 0:
            precision = 1
        else:
            precision = tp / (tp + fp)
        if tp + fn == 0:
            recall = 1
        else:
            recall = tp / (tp + fn)
        precisions.append(precision)
        recalls.append(recall)
    return precisions, recalls


def get_precision_recall(div_value, Y_test, probas):
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

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)

    return precision, recall


def get_all_precisions_recalls(div_values, Y_test, probas):
    precisions = []
    recalls = []
    for div_value in div_values:
        buff = get_precision_recall(div_value, Y_test, probas)
        precisions.append(buff[0])
        recalls.append(buff[1])
    return precisions, recalls


def build_auc_pr(recalls, precisions, title='PR Curve'):
    plt.title(title, fontsize=12)
    plt.xlabel('recall', fontsize=8)
    plt.ylabel('precision', fontsize=8)
    plt.plot(recalls, precisions, 'b', recalls, [1 - i for i in recalls], 'r')
    plt.xlim(0, 1.2)
    plt.ylim(0, 1.2)
    plt.show()
