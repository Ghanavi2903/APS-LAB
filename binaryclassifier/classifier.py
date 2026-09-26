import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

class BreastCancerClassifier:
    def __init__(self):
        self.model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
        self.probablities = None
        self.actual_malignent = None

    def train(self, X_train, y_train):
        print("\n--- Training Model ---")
        self.model.fit(X_train, y_train)
        print("Model trained successfully.")

    def predict_probabilities(self, X_test, y_test):
        print("\n--- Predicting Probabilities ---")
        self.probablities = self.model.predict_proba(X_test)
        self.actual_malignent = (y_test.values == 0).astype(int) # Assuming 0 is malignant based on your notebook
        print("First 5 probability predictions (malignant, benign):\n", self.probablities[:5])

    def evaluate_thresholds(self, thresholds=[0.10, 0.30, 0.50, 0.70, 0.90]):
        print("\n--- Evaluating Model Performance at Different Thresholds ---")
        threshold_results = []

        for threshold in thresholds:
            predictions = (self.probablities[:, 0] >= threshold).astype(int)
            tn, fp, fn, tp = confusion_matrix(self.actual_malignent, predictions, labels=[0, 1]).ravel()
            
            accuracy = accuracy_score(self.actual_malignent, predictions)
            precision = precision_score(self.actual_malignent, predictions, zero_division=0)
            recall = recall_score(self.actual_malignent, predictions, zero_division=0)
            f1 = f1_score(self.actual_malignent, predictions, zero_division=0)

            threshold_results.append({
                "Threshold": threshold,
                "True Negatives (tn)": tn,
                "False Positives (fp)": fp,
                "False Negatives (fn)": fn,
                "True Positives (tp)": tp,
                "Accuracy": accuracy,
                "Precision": precision,
                "Recall": recall,
                "F1 Score": f1
            })

        threshold_table = pd.DataFrame(threshold_results)
        print("\nThreshold Evaluation Table:")
        print(threshold_table.to_string()) # Use print to show in console, or you can return it to main
        return threshold_table