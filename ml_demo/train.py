import os
import pickle
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


def train():
    print("Generating synthetic data...")
    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training XGBoost model...")
    model = xgb.XGBClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    with open("models/xgb_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved to models/xgb_model.pkl")


if __name__ == "__main__":
    train()
