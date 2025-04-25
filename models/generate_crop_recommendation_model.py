import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv('data/soil_data.csv')  # Ensure this file exists in your data directory

# Features and target
X = data[['Region', 'Soil', 'LandArea']]  # Replace with actual feature names
X = pd.get_dummies(X, columns=['Region', 'Soil'])  # Encode categorical variables
y = data['Crop']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model as crop_recommendation.pkl
with open('models/crop_recommendation.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Crop recommendation model saved successfully.")