from dataloader import DataLoader
from classifier import BreastCancerClassifier

def main():
    # Initialize and load data
    data_loader = DataLoader()
    data_loader.load_and_split_data()
    X_train, X_test, y_train, y_test, target_names = data_loader.get_data()

    # Initialize and train classifier
    classifier = BreastCancerClassifier()
    classifier.train(X_train, y_train)

    # Make predictions and evaluate
    classifier.predict_probabilities(X_test, y_test)
    classifier.evaluate_thresholds()

if __name__ == "__main__":
    main()
