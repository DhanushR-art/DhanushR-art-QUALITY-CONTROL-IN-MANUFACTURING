# create_defect_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Create a dummy dataset
# Replace this with your real dataset
data = {
    'feature1': [1, 2, 3, 4, 5, 6],
    'feature2': [7, 8, 9, 10, 11, 12],
    'defect': [0, 1, 0, 1, 0, 1]  # 0 = no defect, 1 = defect
}
df = pd.DataFrame(data)

# Step 2: Split into features (X) and target (y)
X = df[['feature1', 'feature2']]
y = df['defect']

# Step 3: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Evaluate (optional)
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Step 6: Save the model
import os
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/defect_model.pkl")

print("Model saved as models/defect_model.pkl")
