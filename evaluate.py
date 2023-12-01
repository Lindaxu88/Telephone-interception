from plot import Confusion_matrix, Roc_Curve
from sklearn.metrics import accuracy_score, f1_score


def eva_model(model, model_name, X_test, y_test):
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    interception_count = sum(pred == 1)
    interception_rate = interception_count / len(pred)
    Confusion_matrix(predicted_labels=pred, true_labels=y_test, model_name=model_name)
    Roc_Curve(predicted_labels=pred, true_labels=y_test, model_name=model_name)

    print("Interception accuracy of ",model_name, "is:", acc, "F1 score of",model_name, "is:", f1, "Interception rate of ",model_name, "is:", interception_rate)
