from flask import Flask, render_template, request, jsonify
from utils.prediction import predict_prices
from utils.recommendation import recommend_crops
from utils.marketplace import fetch_marketplace_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crop_price', methods=['GET', 'POST'])
def crop_price():
    if request.method == 'POST':
        crop = request.form['crop']
        region = request.form['region']
        predictions = predict_prices(crop, region)
        return jsonify(predictions)
    return render_template('crop_price.html')

@app.route('/crop_recommendation', methods=['GET', 'POST'])
def crop_recommendation():
    if request.method == 'POST':
        region = request.form['region']
        soil = request.form['soil']
        land_area = float(request.form['land_area'])
        recommendations = recommend_crops(region, soil, land_area)
        return jsonify(recommendations)
    return render_template('crop_recommendation.html')

@app.route('/marketplace', methods=['GET'])
def marketplace():
    data = fetch_marketplace_data()
    return render_template('marketplace.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
