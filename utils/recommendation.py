import pandas as pd
import pickle

def recommend_crops(region, soil, land_area):
    # Load the recommendation model
    model = pickle.load(open('models/crop_recommendation.pkl', 'rb'))
    
    # Prepare input data
    input_data = pd.DataFrame({
        'Region': [region],
        'Soil': [soil],
        'LandArea': [land_area]
    })
    
    # Get recommendations
    recommendations = model.predict(input_data)
    return recommendations
