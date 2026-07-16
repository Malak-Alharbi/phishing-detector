import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


data = pd.read_csv('features.csv')


X = data.drop('label', axis=1)
y = data['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model trained successfully!")
print(f"Accuracy: {accuracy * 100:.2f}%")


joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")