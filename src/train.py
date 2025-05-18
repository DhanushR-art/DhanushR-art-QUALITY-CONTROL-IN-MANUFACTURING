# src/train.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Define file paths
data_path = os.path.join("..", "data", "defects_data.csv")
model_path = os.path.join("..", "models", "defect_model.pkl")

# Load the dataset
df = pd.read_csv(data_path)

# Preprocess categorical data
label_encoders = {}
categorical_cols = ['defect_type', 'defect_location', 'severity', 'inspection_method']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Save encoders for future use

# Define features and target
X = df[["defect_type", "defect_location", "repair_cost", "severity", "inspection_method"]]  # Features
y = df["defect_type"]  # Predicting defect type (or choose another target)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model
predictions = clf.predict(X_test)
acc = accuracy_score(y_test, predictions)
print(f"Accuracy: {acc:.2f}")

# Save the model and encoders
os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump({
    'model': clf,
    'label_encoders': label_encoders
}, model_path)
print(f"Model saved to {model_path}")