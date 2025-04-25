# Preprocessing logic for ML models

import pandas as pd
import numpy as np

def preprocess_price_data(data, crop, region):
    """
    Preprocess historical price data for the given crop and region.
    """
    filtered_data = data[(data['Crop'] == crop) & (data['Region'] == region)]
    return filtered_data

def preprocess_recommendation_data(data, region, soil, land_area):
    """
    Prepare data for the crop recommendation model.
    """
    data['Region'] = region
    data['Soil'] = soil
    data['LandArea'] = land_area
    return data
