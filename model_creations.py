import io
import sys
import time
import numpy as np
import xgboost as xgb
from tqdm import tqdm
from sklearn.svm import SVC
from graph_plotter import *
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

class LogisticRegressionWithProgress(LogisticRegression):
    def fit(self, X, y):
        # Initiate tqdm progress bar
        with tqdm(total=self.max_iter, desc="Training Progress", unit="iter") as pbar:
            # Callback function to update progress
            def update_progress(*args):
                pbar.update(1)

            # Use the 'callback' parameter in sklearn to update progress
            super().fit(X, y, callback=update_progress)

def logistic_regression(X_train, X_test, y_train, y_test):
    model = LogisticRegression(
        max_iter=1000, 
        multi_class='multinomial', 
        solver='lbfgs', 
        verbose=2, 
        tol=0.000001
        )
    model.fit(X_train, y_train)
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="Logistic Regression Train Confusion Matrix", save_path="logistic_regression_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="Logistic Regression Test Confusion Matrix", save_path="logistic_regression_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="Logistic Regression Train ROC Curve", save_path="logistic_regression_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="Logistic Regression Test ROC Curve", save_path="logistic_regression_test_roc_curve.png")
    return model, test_accuracy

def decision_tree(X_train, X_test, y_train, y_test, input_size):
    model = DecisionTreeClassifier(random_state=input_size+1)
    model.fit(X_train, y_train)
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="Decision Tree Train Confusion Matrix", save_path="decision_tree_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="Decision Tree Test Confusion Matrix", save_path="decision_tree_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="Decision Tree Train ROC Curve", save_path="decision_tree_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="Decision Tree Test ROC Curve", save_path="decision_tree_test_roc_curve.png")
    return model, test_accuracy

def random_forest(X_train, X_test, y_train, y_test, input_size):
    model = RandomForestClassifier(
        n_estimators=100, 
        random_state=len(y_test),
        verbose=1
        )
    model.fit(X_train, y_train)
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="Random Forest Train Confusion Matrix", save_path="random_forest_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="Random Forest Test Confusion Matrix", save_path="random_forest_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="Random Forest Train ROC Curve", save_path="random_forest_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="Random Forest Test ROC Curve", save_path="random_forest_test_roc_curve.png")
    return model, test_accuracy

def gradient_boosting(X_train, X_test, y_train, y_test, input_size):
    model = GradientBoostingClassifier(
        n_estimators=100, 
        random_state=input_size+1, 
        verbose=1
        )
    model.fit(X_train, y_train)
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="Gradient Boosting Train Confusion Matrix", save_path="gradient_boosting_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="Gradient Boosting Test Confusion Matrix", save_path="gradient_boosting_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="Gradient Boosting Train ROC Curve", save_path="gradient_boosting_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="Gradient Boosting Test ROC Curve", save_path="gradient_boosting_test_roc_curve.png")
    return model, test_accuracy

def support_vector_machine(X_train, X_test, y_train, y_test, input_size):
    model = SVC(
        kernel='linear', 
        random_state=input_size+1
        )
    # Create a tqdm progress bar with an estimated number of steps
    progress_bar = tqdm(desc="Training SVC", total=len(y_test), unit="step")
    # Redirect stdout to capture the verbose output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    # Start the training process
    try:
        model.fit(X_train, y_train)
        # Continuously capture the output and update the progress bar
        while True:
            output = sys.stdout.getvalue()
            if "optimization finished" in output:
                break
            progress_bar.update(1)
            time.sleep(0.1)  # Small sleep to reduce CPU usage
    finally:
        # Restore stdout and close progress bar
        sys.stdout = old_stdout
        progress_bar.close()
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="SVM Train Confusion Matrix", save_path="svm_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="SVM Test Confusion Matrix", save_path="svm_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="SVM Train ROC Curve", save_path="svm_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="SVM Test ROC Curve", save_path="svm_test_roc_curve.png")
    return model, test_accuracy

def neural_network(X_train, X_test, y_train, y_test, input_size):
    model = MLPClassifier(
        hidden_layer_sizes=(64, 64), 
        max_iter=500, 
        random_state=input_size+1,
        verbose=True
        )
    model.fit(X_train, y_train)
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="Neural Network Train Confusion Matrix", save_path="neural_network_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="Neural Network Test Confusion Matrix", save_path="neural_network_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="Neural Network Train ROC Curve", save_path="neural_network_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="Neural Network Test ROC Curve", save_path="neural_network_test_roc_curve.png")
    return model, test_accuracy

def xgboost_classifier(X_train, X_test, y_train, y_test, input_size):
    model = xgb.XGBClassifier(
        n_estimators=100, 
        use_label_encoder=False, 
        eval_metric='mlogloss', 
        random_state=input_size+1,
        verbose=True
        )
    model.fit(X_train, y_train)
    # Predicted classes for training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # Accuracy scores for training and testing
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    # Probability Scores for training and testing data
    y_score_train = model.predict_proba(X_train)
    y_score_test = model.predict_proba(X_test)
    # Plot Confusion Matrix for both
    plot_confusion_matrix(y_train, y_train_pred, title="XG Boost Train Confusion Matrix", save_path="xgboost_train_confusion_matrix.png")
    plot_confusion_matrix(y_test, y_test_pred, title="XG Boost Test Confusion Matrix", save_path="xgboost_test_confusion_matrix.png")
    # Plot ROC Curve for both
    plot_roc_curve(y_train, y_score_train, num_classes=15, title="XG Boost Train ROC Curve", save_path="xgboost_train_roc_curve.png")
    plot_roc_curve(y_test, y_score_test, num_classes=15, title="XG Boost Test ROC Curve", save_path="xgboost_test_roc_curve.png")
    return model, test_accuracy
