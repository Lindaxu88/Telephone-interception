import os.path

from data import get_Data
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from plot import Confusion_matrix, Roc_Curve
from sklearn.neural_network import MLPClassifier
from evaluate import eva_model

x_data, y_data = get_Data(data_type="train")

X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)

logistic_regression_model = LogisticRegression()

clf = DecisionTreeClassifier()

knn = KNeighborsClassifier(n_neighbors=5)

svm_classifier = SVC(kernel='linear', C=1.0)

nb_classifier = MultinomialNB()

bp = MLPClassifier()


def train_half():
    logistic_regression_model.fit(X_train, y_train)
    clf.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    svm_classifier.fit(X_train, y_train)
    nb_classifier.fit(X_train, y_train)
    bp.fit(X_train, y_train)

    eva_model(logistic_regression_model, "logistic", X_test, y_test)
    eva_model(clf, "clf", X_test, y_test)
    eva_model(knn, "KNN", X_test, y_test)
    eva_model(svm_classifier, "SVM", X_test, y_test)
    eva_model(nb_classifier, "NaiveBayes", X_test, y_test)
    eva_model(bp, "BP", X_test, y_test)


def train_all():
    model_dir = 'models'
    x_data, y_data = get_Data(data_type="train")
    logistic_regression_model.fit(x_data, y_data)
    log_model_path = os.path.join(model_dir, 'logistic.pkl')
    joblib.dump(logistic_regression_model, log_model_path)
    clf.fit(x_data, y_data)
    clf_model_path = os.path.join(model_dir, 'clf.pkl')
    joblib.dump(clf, clf_model_path)
    knn.fit(x_data, y_data)
    knn_model_path = os.path.join(model_dir, 'knn.pkl')
    joblib.dump(knn, knn_model_path)
    svm_classifier.fit(x_data, y_data)
    svm_model_path = os.path.join(model_dir, 'svm.pkl')
    joblib.dump(svm_classifier, svm_model_path)
    nb_classifier.fit(x_data, y_data)
    nb_model_path = os.path.join(model_dir, 'nb.pkl')
    joblib.dump(nb_classifier, nb_model_path)
    bp.fit(x_data, y_data)
    bp_model_path = os.path.join(model_dir, 'bp.pkl')
    joblib.dump(bp, bp_model_path)


if __name__ == '__main__':
    train_half()
