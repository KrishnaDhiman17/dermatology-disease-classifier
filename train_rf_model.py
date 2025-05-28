import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
df = pd.read_csv('CO22340_dermatology_database_1.csv')

# Clean the data
df = df[df['age'] != '?']  # Remove rows with missing age
df['age'] = df['age'].astype(int)  # Convert age to integer

# Separate features and target
X = df.drop(['age', 'class'], axis=1)
y = df['class']   # <--- TARGET IS 'class'

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

# Save the model
joblib.dump(model, 'classification_model.pkl')
print("✅ Model saved as 'classification_model.pkl'")
