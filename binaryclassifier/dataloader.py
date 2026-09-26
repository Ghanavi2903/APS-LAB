import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


class DataLoader:
    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.target_names = None

    def load_and_split_data(self):
        data = load_breast_cancer()

        self.X = pd.DataFrame(
            data.data,
            columns=data.feature_names
        )

        self.y = pd.Series(
            (data.target == 0).astype(int),
            name="malignant"
        )

        self.target_names = data.target_names

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X,
            self.y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=self.y
        )

        print("Data loaded and split successfully.")
        self.display_data_info()

    def display_data_info(self):
        print("\n--- Data Information ---")
        print("Target value counts:")
        print(self.y.value_counts())

        print("Feature matrix shape:", self.X.shape)
        print("Target shape:", self.y.shape)
        print("Class names:", self.target_names)

        print("\nTraining size:", len(self.y_train))
        print("Testing size:", len(self.y_test))

    def get_data(self):
        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
            self.target_names
        )