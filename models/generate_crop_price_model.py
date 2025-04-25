import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('data/price_data.csv')  # Ensure this file exists in your data directory

# Features and target
X = data[['Feature1', 'Feature2']]  # Replace with actual feature names
y = data['Price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model as crop_price_model.pkl
with open('models/crop_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Crop price prediction model saved successfully.")

with open('models/crop_price_model.pkl', 'rb') as file:
    crop_price_model = pickle.load(file)