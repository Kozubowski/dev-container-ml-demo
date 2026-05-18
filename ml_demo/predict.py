import os
import pickle
import pandas as pd
from sklearn.datasets import make_classification


def predict():
    print("Loading model...")
    with open("models/xgb_model.pkl", "rb") as f:
        model = pickle.load(f)

    print("Generating new unseen data for prediction...")
    X_new, _ = make_classification(n_samples=100, n_features=10, random_state=99)

    print("Making predictions...")
    predictions = model.predict(X_new)

    os.makedirs("predicted_data", exist_ok=True)
    columns = [f"feature_{i}" for i in range(10)]
    df = pd.DataFrame(X_new, columns=columns)
    df["prediction"] = predictions

    output_path = "predicted_data/predictions.csv"
    df.to_csv(output_path, index=False)
    print(f"Predictions successfully saved to {output_path}")


if __name__ == "__main__":
    predict()
