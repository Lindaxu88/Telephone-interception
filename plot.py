import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc


def Confusion_matrix(true_labels, predicted_labels, model_name):

    file = "eva//" + model_name + "_confusion.png"
    confusion = confusion_matrix(true_labels, predicted_labels)
    sns.set(font_scale=1)
    plt.figure(figsize=(7, 5))
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Negative', 'Positive'],
                yticklabels=['Negative', 'Positive'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.savefig(file)
    return 0


def Roc_Curve(true_labels, predicted_labels, model_name):
    
    file = "eva//" + model_name + "_ROC.png"
    fpr, tpr, _ = roc_curve(true_labels, predicted_labels,pos_label=1)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.savefig(file)
    plt.show()
    return 0


if __name__ == '__main__':
    Roc_Curve([1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 1, 0, 0], "linear")
